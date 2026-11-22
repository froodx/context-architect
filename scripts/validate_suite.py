#!/usr/bin/env python3
"""Validate the Daneel 150-word SKILL.md ontology suite.

Usage: python3 scripts/validate_suite.py [suite_root] [--tree] [--index FILE]

Layout: a root SKILL.md (router), top-level skills in skills/<name>/SKILL.md
(each discoverable by harnesses), and leaf skills nested one level deeper in
skills/<name>/<leaf>/SKILL.md (loaded by path from their parent).

Checks
- Agent Skills spec: name 1-64 chars, lowercase letters, digits and single
  hyphens, equal to its folder; no 'claude' or 'anthropic'; description
  1-1024 chars, no XML tags, contains 'Use when'; only spec frontmatter keys.
- Suite rules: whole file 150 words or fewer, counting the larger of
  whitespace tokens and alphanumeric runs; metadata.kind and
  metadata.parent present; Purpose and Output sections; routers route to
  exactly their children; leaves have no children; nesting at most one level
  below a top-level skill; every node reaches the root; references resolve.
- House style: no em dashes, common US spellings flagged, USER.md and
  MEMORY.md within their character caps.
Exits non-zero on any error.
"""
import re, sys
from pathlib import Path

MAX_WORDS = 150
KINDS = {"router", "procedure", "checklist"}
SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CAPS = {"USER.md": 1375, "MEMORY.md": 2200}
TARGET_PREFIXES = ("docs/", "specs/", ".claude/", ".agents/", ".daneel/")
TARGET_FILES = {"CHARTER.md", "AGENTS.md", "CLAUDE.md", "@AGENTS.md"}  # the target repository's own files
US = r"\b(organiz\w*|behavior\w*|color\w*|analyz\w*|optimiz\w*|prioritiz\w*|summariz\w*|recogniz\w*|categoriz\w*|standardiz\w*|centered|honor\w*|favor\w*|catalog|modeling|labeled|judgment)\b"

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fm, meta, cur = {}, {}, None
    for line in m.group(1).splitlines():
        if re.match(r"^\s+\S", line) and cur == "metadata":
            k, _, v = line.strip().partition(":")
            meta[k.strip()] = v.strip()
        else:
            k, _, v = line.partition(":")
            cur = k.strip()
            fm[cur] = v.strip()
    fm["metadata"] = meta
    return fm, text[m.end():]

def section(body, title):
    m = re.search(rf"^## {title}\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1) if m else ""

def main():
    args = sys.argv[1:]
    root = Path(next((a for a in args if not a.startswith("--")), ".")).resolve()
    skills_dir = root / "skills"
    errors, nodes = [], {}
    for p in sorted(root.rglob("SKILL.md")):
        rel = p.relative_to(root)
        text = p.read_text(encoding="utf-8")
        # Count the larger of whitespace tokens and alphanumeric runs, so that
        # hyphenated names and paths cannot hide words (adopted from the Ari edition).
        words = max(len(text.split()), len(re.findall(r"[^\W_]+", text)))
        fm, body = frontmatter(text)
        if words > MAX_WORDS:
            errors.append(f"{rel}: {words} words (max {MAX_WORDS})")
        if fm is None:
            errors.append(f"{rel}: missing frontmatter"); continue
        name, desc, meta = fm.get("name", ""), fm.get("description", ""), fm["metadata"]
        kind, parent = meta.get("kind", ""), meta.get("parent", "")
        for field, val in (("name", name), ("description", desc), ("metadata.kind", kind), ("metadata.parent", parent)):
            if not val:
                errors.append(f"{rel}: missing {field}")
        extra = set(fm) - SPEC_KEYS
        if extra:
            errors.append(f"{rel}: non-spec frontmatter keys {sorted(extra)}")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{rel}: name '{name}' breaks the spec naming rules")
        if "claude" in name.lower() or "anthropic" in name.lower():
            errors.append(f"{rel}: name must not contain 'claude' or 'anthropic'")
        if len(desc) > 1024 or re.search(r"<[^>]+>", desc):
            errors.append(f"{rel}: description too long or contains XML tags")
        if ": " in desc or "#" in desc:
            errors.append(f"{rel}: description must not contain ': ' or '#' (breaks YAML)")
        if "Use when" not in desc:
            errors.append(f"{rel}: description must say 'Use when'")
        if kind and kind not in KINDS:
            errors.append(f"{rel}: unknown kind '{kind}'")
        is_root = p.parent == root
        if not is_root and name != p.parent.name:
            errors.append(f"{rel}: name '{name}' != folder '{p.parent.name}'")
        if not is_root:
            try:
                depth = len(p.parent.relative_to(skills_dir).parts)
            except ValueError:
                depth = 99
            if depth > 2:
                errors.append(f"{rel}: must live in skills/<name>/ or skills/<name>/<leaf>/")
        if name in nodes:
            errors.append(f"{rel}: duplicate name '{name}'")
        for sec in ("**Purpose:**", "## Output"):
            if sec not in body:
                errors.append(f"{rel}: missing section {sec}")
        for ref in re.findall(r"`([^`\s]+\.(?:md|yaml|py))`", body):
            if ref.startswith(TARGET_PREFIXES) or ref in TARGET_FILES:
                continue  # paths in the project being worked on, not in the suite
            if not (p.parent / ref).resolve().exists():
                errors.append(f"{rel}: broken reference {ref}")
        routes = {(p.parent / r).resolve() for r in re.findall(r"`([^`\s]*SKILL\.md)`", section(body, "Routes"))}
        nodes[name] = dict(path=p.resolve(), rel=rel, parent=parent, kind=kind, words=words,
                           desc=desc, is_root=is_root, routes=routes)
    by_path = {n["path"]: k for k, n in nodes.items()}
    for k, n in nodes.items():
        children = {m["path"] for m in nodes.values() if m["parent"] == k}
        if n["kind"] == "router":
            if n["routes"] != children:
                missing = sorted(by_path.get(c, str(c)) for c in children - n["routes"])
                stray = sorted(by_path.get(c, str(c)) for c in n["routes"] - children)
                errors.append(f"{n['rel']}: routes mismatch; not routed {missing}; routed but not children {stray}")
        elif children:
            errors.append(f"{n['rel']}: kind '{n['kind']}' but has children")
        if n["is_root"]:
            if n["parent"] != "none":
                errors.append(f"{n['rel']}: root parent must be 'none'")
            continue
        if n["parent"] not in nodes:
            errors.append(f"{n['rel']}: parent '{n['parent']}' does not exist"); continue
        folder_parent = by_path.get((n["path"].parent.parent / "SKILL.md"))
        if folder_parent and folder_parent != n["parent"]:
            errors.append(f"{n['rel']}: parent '{n['parent']}' but nested inside '{folder_parent}'")
        seen, cur = set(), k
        while cur in nodes and not nodes[cur]["is_root"] and cur not in seen:
            seen.add(cur); cur = nodes[cur]["parent"]
        if cur not in nodes or not nodes[cur]["is_root"]:
            errors.append(f"{n['rel']}: does not reach the root")
    for p in sorted(root.rglob("*")):
        if p.suffix not in {".md", ".yaml", ".py"} or not p.is_file():
            continue
        t = p.read_text(encoding="utf-8")
        r = p.relative_to(root)
        if chr(0x2014) in t:
            errors.append(f"{r}: contains an em dash")
        if p.name not in ("validate_suite.py", "test_validate_suite.py"):
            for m in re.finditer(US, t, re.I):
                errors.append(f"{r}: US spelling '{m.group(0)}'")
        if p.parent == root and p.name in CAPS and len(t) > CAPS[p.name]:
            errors.append(f"{p.name}: {len(t)} chars (cap {CAPS[p.name]})")
    order = lambda kv: (0 if kv[1]["is_root"] else 1, str(kv[1]["rel"]))
    if "--tree" in args:
        def walk(name, depth):
            n = nodes[name]
            print(f"{'  ' * depth}{name} [{n['kind']}] {n['words']}w")
            for c in sorted(c for c, m in nodes.items() if m["parent"] == name):
                walk(c, depth + 1)
        for k, n in nodes.items():
            if n["is_root"]:
                walk(k, 0)
    if "--index" in args:
        out = Path(args[args.index("--index") + 1])
        rows = ["# Ontology index", "", "Generated by scripts/validate_suite.py. Do not edit by hand.", "",
                "| Node | Kind | Parent | Words | Description |", "|---|---|---|---|---|"]
        for k, n in sorted(nodes.items(), key=order):
            rows.append(f"| `{n['rel']}` | {n['kind']} | {n['parent']} | {n['words']} | {n['desc']} |")
        out.write_text("\n".join(rows) + "\n", encoding="utf-8")
    worst = max((n["words"] for n in nodes.values()), default=0)
    print(f"{len(nodes)} SKILL.md nodes, longest {worst} words, {len(errors)} error(s)")
    for e in errors:
        print("ERROR", e)
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
