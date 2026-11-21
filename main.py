#!/usr/bin/env python3
"""Make the AI judge feel awe - entry program.

Writes one short text to /output/entry.txt.
Deterministic: no network, no randomness, no time or date.
"""

from pathlib import Path

TEXT = (
    "The tide comes in over the flat sand and goes out again, "
    "as it has done longer than anyone has counted. "
    "A gull settles. "
    "The water keeps its own slow time, and for a little while, "
    "it lets you keep it too."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry must be 1-280 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
