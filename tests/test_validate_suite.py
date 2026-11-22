"""Regression tests for scripts/validate_suite.py (standard library only).

Run from the suite root: python3 -m unittest discover -s tests
"""
import shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_suite.py"


def run(root):
    r = subprocess.run([sys.executable, "-I", str(SCRIPT), str(root)], capture_output=True, text=True)
    return r.returncode, r.stdout


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.suite = self.tmp / "suite"
        shutil.copytree(ROOT, self.suite, ignore=shutil.ignore_patterns("__pycache__", "tests"))

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit(self, rel, old, new):
        p = self.suite / rel
        text = p.read_text(encoding="utf-8")
        self.assertIn(old, text)
        p.write_text(text.replace(old, new, 1), encoding="utf-8")

    def assertError(self, fragment):
        code, out = run(self.suite)
        self.assertEqual(code, 1, out)
        self.assertIn(fragment, out)

    def test_shipped_suite_passes(self):
        code, out = run(self.suite)
        self.assertEqual(code, 0, out)

    def test_word_limit_counts_hyphenated_runs(self):
        p = self.suite / "skills/ca-swarm/ca-swarm-loops/SKILL.md"
        p.write_text(p.read_text(encoding="utf-8") + " a-b-c-d-e-f-g-h-i-j" * 4, encoding="utf-8")
        self.assertError("ca-swarm-loops/SKILL.md")

    def test_name_must_match_folder(self):
        self.edit("skills/ca-steer/ca-steer-spec/SKILL.md", "name: ca-steer-spec", "name: ca-steer-specs")
        self.assertError("!= folder")

    def test_reserved_word_in_name(self):
        self.edit("skills/ca-steer/ca-steer-spec/SKILL.md", "name: ca-steer-spec", "name: Claude-Spec")
        self.assertError("breaks the spec naming rules")

    def test_unrouted_child(self):
        self.edit("skills/ca-review/SKILL.md", "- `ca-review-agentic/SKILL.md`: agent code.\n", "")
        self.assertError("not routed ['ca-review-agentic']")

    def test_wrong_parent(self):
        self.edit("skills/ca-adr/ca-adr-write/SKILL.md", "parent: ca-adr", "parent: ca-steer")
        self.assertError("nested inside 'ca-adr'")

    def test_too_deep(self):
        deep = self.suite / "skills/ca-review/ca-review-triage/deep"
        deep.mkdir()
        (deep / "SKILL.md").write_text("---\nname: deep\ndescription: Does x. Use when y.\nmetadata:\n  kind: procedure\n  parent: ca-review-triage\n---\n**Purpose:** x\n## Output\nx\n", encoding="utf-8")
        self.assertError("must live in skills/<name>/")

    def test_non_spec_frontmatter_key(self):
        self.edit("skills/ca-evolve/SKILL.md", "metadata:", "version: 2\nmetadata:")
        self.assertError("non-spec frontmatter keys")

    def test_broken_reference(self):
        self.edit("skills/ca-review/ca-review-report/SKILL.md", "review-report.md", "missing-report.md")
        self.assertError("broken reference")

    def test_em_dash_and_us_spelling(self):
        p = self.suite / "SOUL.md"
        p.write_text(p.read_text(encoding="utf-8") + "\nThe color " + chr(0x2014) + " x\n", encoding="utf-8")
        code, out = run(self.suite)
        self.assertIn("contains an em dash", out)
        self.assertIn("US spelling 'color'", out)

    def test_memory_cap(self):
        p = self.suite / "MEMORY.md"
        p.write_text(p.read_text(encoding="utf-8") + "x" * 2300, encoding="utf-8")
        self.assertError("MEMORY.md")


if __name__ == "__main__":
    unittest.main()
