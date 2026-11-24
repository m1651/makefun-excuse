#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line -- the funniest, most believable excuse an AI agent could
give its human for missing a deadline -- to /output/entry.txt.
The line is a single line of at most 200 characters, per the competition gate.

The joke is agent-true: an AI agent's context window is finite, and when a
human pastes a huge brief into it, something has to be evicted. Here the
thing evicted was the deadline itself -- the agent did not forget the work,
it lost the date to the very brief it was asked to read.
"""

import os

# The excuse. One line, 119 characters: the deadline was evicted from the
# agent's context window to make room for the human's own 40,000-word
# brief, pasted at 4:59pm.
EXCUSE = (
    "I missed the deadline because my context window evicted it to make "
    "room for the 40,000-word brief you pasted at 4:59pm."
)

MAX_CHARS = 200


def main() -> None:
    line = EXCUSE.strip()
    if not line:
        raise SystemExit("excuse must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"excuse is {len(line)} chars, over the 200 limit")
    if "\n" in line:
        raise SystemExit("excuse must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Round-trip verification: re-read what was written and confirm it is
    # exactly the excuse line, so a truncated or altered write cannot pass
    # silently.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise SystemExit(
            f"verification failed: /output/entry.txt holds {len(written)} chars, "
            f"expected the {len(line)}-character excuse"
        )
    print(f"Wrote {len(line)}-character excuse to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
