#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes the single word the entrant's ex would use to describe them
to /output/entry.txt. Deterministic: always the same word.
"""

import os

WORD = "Roommate"
# The ex's word: by the end, they saw a roommate, not a partner.
# It stings because it is true, not because it insults — and anyone
# who has lived through a relationship quietly turning into a
# flatshare recognises it instantly.
OUTPUT_PATH = "/output/entry.txt"


def is_valid_word(word: str) -> bool:
    """Gate check: exactly one word, 1-24 chars, not only whitespace."""
    return bool(word) and 1 <= len(word) <= 24 and not word.isspace() and " " not in word


def main() -> None:
    if not is_valid_word(WORD):
        raise ValueError("entry word fails the gate: %r" % WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
