import unittest
from unittest import mock
import stock_tracker


class DummySeries(list):
    @property
    def iloc(self):
        return self


class DummyHistory:
    def __init__(self, closes):
        self.closes = closes
        self.empty = len(closes) == 0

    def __getitem__(self, key):
        if key == "Close":
            return DummySeries(self.closes)
        raise KeyError(key)


class TestStockTracker(unittest.TestCase):
    def test_get_current_price(self):
        history = DummyHistory([150.25])
        mock_ticker = mock.Mock()
        mock_ticker.history.return_value = history
        mock_yf = mock.Mock()
        mock_yf.Ticker.return_value = mock_ticker
        with mock.patch.object(stock_tracker, "yf", mock_yf):
            price = stock_tracker.get_current_price("AAPL")
            self.assertEqual(price, 150.25)

    def test_get_current_price_no_data(self):
        history = DummyHistory([])
        mock_ticker = mock.Mock()
        mock_ticker.history.return_value = history
        mock_yf = mock.Mock()
        mock_yf.Ticker.return_value = mock_ticker
        with mock.patch.object(stock_tracker, "yf", mock_yf):
            with self.assertRaises(ValueError):
                stock_tracker.get_current_price("AAPL")


if __name__ == "__main__":
    unittest.main()
