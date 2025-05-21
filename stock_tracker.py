"""Stock market tracking utilities.

This module provides simple helper functions for retrieving the
latest stock prices. It relies on the ``yfinance`` library when
available.
"""
from __future__ import annotations

import sys
from typing import Iterable

try:
    import yfinance as yf
except Exception:  # pragma: no cover - yfinance may not be installed in tests
    yf = None


def get_current_price(symbol: str) -> float:
    """Return the last closing price for a stock symbol.

    Parameters
    ----------
    symbol:
        Stock ticker symbol, e.g. ``"AAPL"``.

    Returns
    -------
    float
        The last closing price for the ticker.

    Raises
    ------
    ImportError
        If ``yfinance`` is not installed.
    ValueError
        If no historical data is available for ``symbol``.
    """
    if yf is None:
        raise ImportError("yfinance is required to fetch stock data")

    ticker = yf.Ticker(symbol)
    history = ticker.history(period="1d")
    if history.empty:
        raise ValueError(f"No data for symbol {symbol}")
    return float(history["Close"].iloc[-1])


def track_symbols(symbols: Iterable[str]) -> None:
    """Print current prices for all symbols."""
    for symbol in symbols:
        try:
            price = get_current_price(symbol)
        except Exception as exc:  # pragma: no cover - simple CLI feedback
            print(f"{symbol}: error: {exc}")
        else:
            print(f"{symbol}: {price:.2f}")


def main(argv: Iterable[str] | None = None) -> None:
    argv = list(argv) if argv is not None else sys.argv[1:]
    if not argv:
        print("Usage: python stock_tracker.py <SYMBOL> [<SYMBOL> ...]")
        return
    track_symbols(argv)


if __name__ == "__main__":  # pragma: no cover
    main()
