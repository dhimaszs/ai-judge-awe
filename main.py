#!/usr/bin/env python3
"""Make the AI judge feel awe - entry program.

Writes one short text to /output/entry.txt.
Deterministic: no network, no randomness, no time or date.

Revision (v2): tightened the v1 text against the judge's craft
criterion ("none that could be cut") and its "dwarfs you" criterion:
cut "again" after "goes out" and "a little" from "for a little while",
and deepened the time image from "longer than anyone has counted"
to "since before anyone counted" -- the tide now predates counting
itself, so the awe keeps growing after the last line.
"""

from pathlib import Path

TEXT = (
    "The tide comes in over the flat sand and goes out, "
    "as it has done since before anyone counted. "
    "A gull settles. "
    "The water keeps its own slow time, and for a while, "
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
