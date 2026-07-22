import json
from typing import TYPE_CHECKING

from countdown.__main__ import group_anagrams, load_dictionary

if TYPE_CHECKING:
    from pathlib import Path

    import pytest


def test_load_dictionary(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    fixture = {"abc": ["cab", "bac"]}
    (tmp_path / "dictionary.json").write_text(json.dumps(fixture), encoding="utf-8")
    monkeypatch.setattr("countdown.__main__.files", lambda **_: tmp_path)

    index = load_dictionary()

    assert index == fixture


def test_group_anagrams_basic() -> None:
    index = {"cdnnootuw": ["countdown"]}
    result = group_anagrams("downcount", index, 3)
    assert result == {9: ["countdown"]}


def test_group_anagrams_finds_subwords() -> None:
    index = {
        "cdnnootuw": ["countdown"],
        "cdnotuw": ["downcut"],
        "cdootuw": ["woodcut"],
        "nnootw": ["wonton"],
    }
    result = group_anagrams("downcount", index, 3)
    assert set(result.keys()) == {9, 7, 6}
    assert result[9] == ["countdown"]
    assert set(result[7]) == {"downcut", "woodcut"}
    assert result[6] == ["wonton"]


def test_group_anagrams_no_match() -> None:
    result = group_anagrams("zzz", {}, 3)
    assert result == {}


def test_group_anagrams_results_limit() -> None:
    index = {
        "cdnnootuw": ["countdown"],
        "cdnotuw": ["downcut"],
        "cdootuw": ["woodcut"],
        "nnootw": ["wonton"],
    }
    result = group_anagrams("downcount", index, 2)
    assert set(result.keys()) == {9, 7}
