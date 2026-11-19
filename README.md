# Row Game

A Python reference implementation for a one-dimensional scoring puzzle with a large turn budget. It computes interval gains with prefix sums and batches profitable round trips together, to keep runtime independent of the turn budget.

The implementation maintains the earliest arrival and its score for each position. It runs in quadratic time in the row length and linear space. [Source](row_game.py) · [Public regression examples](test_row_game.py)

Use Python 3.11 or later and run from this directory.

```sh
python3 -m unittest -v
```
