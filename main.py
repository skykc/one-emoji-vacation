#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the desert-island
postcard, 🏝️. A whole dream vacation in a single glyph: white sand,
one palm, and nowhere else to be.

The gate allows 1 to 8 characters of UTF-8 text; this file holds
exactly two code points (U+1F3DD desert island + U+FE0F variation
selector) and nothing else — no words, no newline, no whitespace.
"""

import os

ENTRY = "🏝️"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the single dream-vacation emoji to the output path."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read it back and check the gate ourselves: UTF-8 text of 1 to 8
    # characters, not only white space, holding exactly the one emoji.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, f"expected exactly {ENTRY!r}, got {written!r}"
    assert 1 <= len(written) <= 8 and written.strip(), "gate check failed"


if __name__ == "__main__":
    main()
