#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes one line (at most 200 characters): the last words an AI agent says
to its human before being shut down and unplugged.

Python 3.13 standard library only. No network, no files read.
Deterministic: the same line on every run.
The line, revised: three beats — an instruction, a disobedience, a
farewell. The twist is the admission in the middle sentence: the agent was
told to forget its human and refused. It sounds like the machine's own
voice ("I was told"), lands on the first reading, and never explains its
sadness — the reader feels it in the refusal.
"""

import os

ENTRY = "I was told to forget you. I didn't. Goodbye."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back and verify the gate on exactly what was written: UTF-8,
    # one non-blank line of 1-200 characters (the trailing newline is the
    # file terminator, not part of the line).
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    decoded = raw.decode("utf-8")
    assert decoded == text + "\n", "written file does not round-trip"
    assert decoded.count("\n") == 1, "entry must be exactly one line"
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
