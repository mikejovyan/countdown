# countdown

A solver for the Countdown letters game.

## Usage

In a Countdown letters game, contestants form the longest word they can from a scramble of nine letters. No letter may be used more often than it appears in the scramble. More information on the rules can be found [here](http://wiki.apterous.org/Letters_game).

`countdown` takes up to nine letters and returns the longest words that can be formed, grouped by length:

```
$ countdown
Enter up to nine letters (or press Enter to quit): gransmith
9 letter words: hamstring
8 letter words: manghirs, marshing, migrants, smarting, thingams, trashing
7 letter words: garnish, gastrin, gratins, harming, hasting, manghir, mantris, margins, martins, mashing, masting, matings, migrant, rahings, rashing, ratings, shaming, sharing, staring, tarnish, thamins, thingam
```

## Dictionary

File | Description
--- | ---
[data/dictionary.txt](data/dictionary.txt) | Word list — one word per line, source of truth
[src/countdown/dictionary.json](src/countdown/dictionary.json) | Runtime index — generated from `dictionary.txt`

The word list is sourced from [here](https://countdownresources.wordpress.com/2018/10/13/complete-list-of-words-ordered-by-how-useful-they-are-for-countdown/).

To regenerate the runtime index after editing the word list:

```
python scripts/generate_dictionary.py
```
