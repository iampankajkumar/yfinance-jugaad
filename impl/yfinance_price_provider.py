from datetime import datetime
import yfinance as yf

from service.stock_price_provider import AbstractStockPriceProvider

class YahooFinanceProvider(AbstractStockPriceProvider):
    def get_ohlc(self, symbol):
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        if data.empty:
            raise ValueError("Invalid symbol or data unavailable = {}",symbol)

        # Strip timezone part
        record_date = str(data.index[-1]).split('+')[0]
        return {
            "recordDate": datetime.strptime(record_date, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d 00:00:00.000"),
            "open": round(float(data['Open'].iloc[-1]), 2),
            "high": round(float(data['High'].iloc[-1]), 2),
            "low": round(float(data['Low'].iloc[-1]), 2),
            "close": round(float(data['Close'].iloc[-1]), 2),
            "ltp": round(float(data['Close'].iloc[-1]), 2),
            "volume": int(data['Volume'].iloc[-1])
        }