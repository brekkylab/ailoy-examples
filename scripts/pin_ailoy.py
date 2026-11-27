"""Point every example at a published ailoy release.

    python3 scripts/pin_ailoy.py 0.3.3

Rewrites the root `Cargo.toml` (the `ailoy` version, and drops `[patch.crates-io]`), each
`*/python/pyproject.toml` (`ailoy-py>=VERSION,<NEXT_MINOR`, and drops its `[tool.uv.sources]` path) and each
`*/node/package.json` (`^VERSION`). Then refresh the lockfiles: `cargo update -p ailoy`, `uv lock`
in each Python folder, `npm install` in each Node folder.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def pin_cargo(version: str) -> None:
    path = ROOT / "Cargo.toml"
    text = path.read_text()
    text = re.sub(r'(?m)^ailoy = "[^"]*"$', f'ailoy = "{version}"', text)
    # The patch block and the comment above it, to the end of the file.
    text = re.sub(r"(?s)\n(#[^\n]*\n)*\[patch\.crates-io\]\n.*\Z", "\n", text)
    path.write_text(text)


def pin_python(path: Path, version: str) -> None:
    text = path.read_text()
    major, minor, _ = version.split(".")
    # Below the next minor, as `virtx>=0.2.0,<0.3` beside it: before 1.0 a minor may break.
    text = re.sub(r'"ailoy-py[^"]*"', f'"ailoy-py>={version},<{major}.{int(minor) + 1}"', text)
    # The comment and path source for ailoy-py; a section left empty goes too.
    text = re.sub(r"(?m)^(#[^\n]*\n)*ailoy-py = \{ path = [^\n]*\n", "", text)
    text = re.sub(r"\n\[tool\.uv\.sources\]\n(?=\n|\[|\Z)", "\n", text)
    path.write_text(text.rstrip("\n") + "\n")


def pin_node(path: Path, version: str) -> None:
    package = json.loads(path.read_text())
    package["dependencies"]["@brekkylab/ailoy"] = f"^{version}"
    path.write_text(json.dumps(package, indent=2) + "\n")


def main() -> None:
    if len(sys.argv) != 2 or not re.fullmatch(r"\d+\.\d+\.\d+", sys.argv[1]):
        sys.exit(__doc__)
    version = sys.argv[1]
    pin_cargo(version)
    for path in sorted(ROOT.glob("*/python/pyproject.toml")):
        pin_python(path, version)
    for path in sorted(ROOT.glob("*/node/package.json")):
        pin_node(path, version)
    print(f"ailoy {version} everywhere; now refresh the lockfiles (see this file's docstring).")


if __name__ == "__main__":
    main()
