"""Countdown letters game solver."""

import json
import logging
from collections import defaultdict
from importlib.resources import files
from itertools import combinations

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger: logging.Logger = logging.getLogger(name=__name__)


def load_dictionary() -> dict[str, list[str]]:
    """Load the pre-built sorted-key index from a JSON file.

    Returns:
        Dict mapping sorted-letter string to list of matching words.

    """
    with (files(anchor="countdown") / "dictionary.json").open(encoding="utf-8") as f:
        return json.load(f)


def group_anagrams(
    letters: str,
    index: dict[str, list[str]],
    results: int,
) -> dict[int, list[str]]:
    """Find and group anagrams by word length, returning the longest groups.

    Args:
        letters: The available letters to form words from.
        index: Sorted-letter key to word list mapping.
        results: Maximum number of length groups to return.

    Returns:
        Dict mapping word length to list of matching words,
        for the top `results` lengths.

    """
    by_length: dict[int, list[str]] = defaultdict(list)
    sorted_letters: list[str] = sorted(letters)
    for length in range(2, len(letters) + 1):
        seen: set[str] = set()
        for combo in combinations(sorted_letters, length):
            key: str = "".join(combo)
            if key in seen:
                continue
            seen.add(key)
            for word in index.get(key, ()):
                by_length[len(word)].append(word)
    top_lengths: list[int] = sorted(by_length.keys(), reverse=True)[:results]
    return {length: by_length[length] for length in top_lengths}


def main(letters: int = 9, results: int = 3) -> None:
    """Run the countdown solver interactively."""
    index: dict[str, list[str]] = load_dictionary()

    while True:
        scramble: str = input(
            "Enter up to nine letters (or press Enter to quit): ",
        ).lower()

        if not scramble:
            break

        if not scramble.isalpha():
            logger.info("Enter letters only.")
            continue

        if len(scramble) > letters:
            logger.info("Enter up to %d letters only", letters)
            continue

        anagrams: dict[int, list[str]] = group_anagrams(scramble, index, results)

        if not anagrams:
            logger.info("There were no anagrams found for those letters")
            continue

        for length, matches in sorted(anagrams.items(), reverse=True):
            logger.info("%d letter words: %s", length, ", ".join(matches))

        logger.info("")


if __name__ == "__main__":
    main()
