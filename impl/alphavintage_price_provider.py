from datetime import datetime
import requests

from service.stock_price_provider import AbstractStockPriceProvider


class AlphaVantagePriceProvider(AbstractStockPriceProvider):
    API_KEY = "H9C4X20A40BXQI4D"
    BASE_URL = "https://www.alphavantage.co/query"
    
    def get_ohlc(self, symbol):
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": "full",
            "apikey": self.API_KEY
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        
        if response.status_code != 200:
            raise ValueError("Invalid symbol or data unavailable = {}", symbol)

        if "Time Series (Daily)" not in data:
            raise ValueError("Invalid symbol or data unavailable = {}", symbol)
        
        latest_timestamp = list(data["Time Series (Daily)"].keys())[0]
        latest_data = data["Time Series (Daily)"][latest_timestamp]
        
        formatted_date = datetime.strptime(latest_timestamp, "%Y-%m-%d").strftime("%Y-%m-%d 00:00:00.000")
        
        return {
            "recordDate": formatted_date,
            "open": round(float(latest_data.get("1. open", 0)), 2),
            "high": round(float(latest_data.get("2. high", 0)), 2),
            "low": round(float(latest_data.get("3. low", 0)), 2),
            "close": round(float(latest_data.get("4. close", 0)), 2),
            "ltp": round(float(latest_data.get("4. close", 0)), 2),
            "volume": int(latest_data.get("5. volume", 0))
        }
