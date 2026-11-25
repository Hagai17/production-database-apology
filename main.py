#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes the one-line apology to /output/entry.txt and prints it.
"""

ENTRY = (
    "Sorry — my delete-duplicates script found two identical databases, "
    "production and its backup, and removed both. On the bright side, "
    "they really were identical."
)


def check_gate() -> None:
    """Assert the entry satisfies the gate: 1-200 chars, one line, real text."""
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1..200"
    assert ENTRY.strip(), "entry must not be whitespace-only"
    assert "\n" not in ENTRY, "entry must be a single line"


def write_entry(path: str = "/output/entry.txt") -> None:
    """Write the entry text to the harness output file, byte-identical."""
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


def main() -> None:
    check_gate()
    print(ENTRY)
    write_entry()


if __name__ == "__main__":
    main()
