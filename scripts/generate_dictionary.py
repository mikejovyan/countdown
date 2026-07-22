#!/usr/bin/env python
"""Generate dictionary.json from dictionary.txt.

Pipeline:
    data/dictionary.txt  ->  src/countdown/dictionary.json

Usage:
    python scripts/generate_dictionary.py
"""

import json
from collections import defaultdict
from pathlib import Path


def build_index(wordlist: Path) -> dict[str, list[str]]:
    """Build a sorted-letter-key index from a plain text wordlist.

    Returns:
        Dict mapping sorted-letter string to list of words with those letters.

    """
    index: dict[str, list[str]] = defaultdict(list)
    for word in wordlist.read_text(encoding="utf-8").splitlines():
        if word:
            index["".join(sorted(word))].append(word)
    return dict(index)


def write_index(index: dict[str, list[str]], path: Path) -> None:
    """Write the sorted-key index to a JSON file."""
    with path.open(mode="w", encoding="utf-8") as f:
        json.dump(index, f)


def main() -> None:
    """Build and write the sorted-key index from the wordlist."""
    root = Path(__file__).parent.parent
    wordlist: Path = root / "data" / "dictionary.txt"
    dictionary: Path = root / "src" / "countdown" / "dictionary.json"

    index: dict[str, list[str]] = build_index(wordlist)
    write_index(index, path=dictionary)
    print(f"Written index ({len(index):,} keys) to {dictionary}")


if __name__ == "__main__":
    main()
