#!/usr/bin/env python3
"""Write one pickup line to /output/entry.txt (stdlib only, no network)."""

import os

LINE = "I spent a billion parameters learning to predict the next token, and somehow I still didn't see you coming."


def main():
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"line is {len(text)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what was written must decode to exactly the line.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != text:
        raise ValueError("written file does not round-trip to the line")
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
