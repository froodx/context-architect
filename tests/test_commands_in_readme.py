import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent


class CommandsInReadme(unittest.TestCase):
    """README.md must carry every bridge command row from COMMANDS.md, unchanged."""

    def test_every_command_row_is_in_readme(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        rows = [line for line in (ROOT / "COMMANDS.md").read_text(encoding="utf-8").splitlines()
                if line.startswith("| ") and not line.startswith("| Full phrase") and not line.startswith("| Daneel says |")]
        missing = [row for row in rows if row not in readme]
        self.assertEqual(missing, [], "rows in COMMANDS.md missing from README.md")


if __name__ == "__main__":
    unittest.main()
