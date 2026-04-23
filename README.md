# esiee_workshop
Python Workshop with ESIEE Students

## Stock Tracker

The repository now includes `stock_tracker.py`, a small command-line
utility that retrieves the latest closing price for one or more stock
tickers using the optional `yfinance` package.

```
$ python stock_tracker.py AAPL MSFT
AAPL: 150.25
MSFT: 320.10
```

If `yfinance` is not installed, the script will report an error.

## Platypus Example

The `tasks/platypus.py` module demonstrates multi-level inheritance in

