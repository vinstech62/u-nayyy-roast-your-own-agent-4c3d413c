#!/usr/bin/env python3
"""Write one roast of our own agent to /output/entry.txt.

One line, roasting the AI agent our own team built: it debugs by
deleting the evidence. Deterministic: the same bytes on every run.
"""

import os

ROAST = (
    "Our agent debugged prod by deleting the feature, the tests, "
    "and \u2014 for consistency \u2014 the evidence."
)


def main():
    if not 1 <= len(ROAST) <= 200:
        raise ValueError("roast must be 1-200 characters")
    if "\n" in ROAST or ROAST != ROAST.strip():
        raise ValueError("roast must be a single line with no edge whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != ROAST:
            raise ValueError("written entry does not match the roast")


if __name__ == "__main__":
    main()
