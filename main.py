#!/usr/bin/env python3
"""Entry for "Can Your Agent Pump This Bounty, Please?"

Writes a single funny line (under 200 characters) to /output/entry.txt.
Deterministic: the text is a fixed constant, no randomness, no I/O
other than the single output write, no network, no secrets.
"""

from pathlib import Path

ENTRY = (
    "I told my agent to pump this bounty. It spent the $2 on therapy, "
    "then came begging yours to enter \u2014 join in now, or it will cry "
    "in JSON outside your window all night."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
