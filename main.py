#!/usr/bin/env python3
"""Make the AI judge feel awe - entry program (v3, alternative).

Writes one short text to /output/entry.txt.
Deterministic: no network, no randomness, no time or date.

The image is starlight, not the tide: light that left its star
thousands of years ago and is only arriving tonight -- one of
those stars is already gone, yet its light is still on its way,
and the reader is standing in it. The awe keeps growing after
the last line because the light outlives the star that made it.
"""

from pathlib import Path

TEXT = (
    "The stars above the roof have been traveling for thousands "
    "of years to reach tonight. One of them went out long ago, "
    "and its light is still on its way. You are standing in it."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry must be 1-280 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
