# Deprecation: the d_ prefix

Two steps, so nothing is deleted on a hunch and nothing lingers for ever.

1. **Mark.** Code that should no longer be used, but is not yet proven safe to remove, gets a `d_` prefix on its name: file, module, function, class or setting (`d_legacy_export.py`, `d_send_receipt()`). Existing callers inside the repository are updated to the new name in the same commit. Also mark it the way the language expects, so tools and people see it: a docstring or comment saying what to use instead, and a runtime deprecation warning where the language has one (Python `warnings.warn(..., DeprecationWarning)`, JavaScript `/** @deprecated */`).
2. **Kill.** On every "carry on" and every "phasers on kill", Daneel reviews the `d_` items. Any proven unused (no references, imports, dynamic or entry-point use, config or docs) is removed, with tests green, an independent check, and one revertable commit each. This needs no approval; it is code, not data.

House rules (written into the `AGENTS.md` managed block):
- Never add a new use of a `d_` item. Use what its note points to.
- New code never starts with `d_`.

When not to rename: a name that people or systems outside the repository call (a public API, a CLI flag, an HTTP route, a published package). Renaming would break them. Keep the name, add the deprecation note and warning, and list it in the managed block as deprecated instead; removing it later is a public interface break, which the charter gates.

Proportion: mark only what is genuinely superseded or suspected dead. Do not sweep the codebase for things to deprecate.
