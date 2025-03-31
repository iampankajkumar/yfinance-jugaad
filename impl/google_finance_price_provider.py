import requests
from service.stock_price_provider import AbstractStockPriceProvider


class GoogleFinancePriceProvider(AbstractStockPriceProvider):
    BASE_URL = "https://www.google.com/finance/quote/{}"
    
    def get_ohlc(self, symbol):
        url = self.BASE_URL.format(symbol)
        response = requests.get(url)
        
        if response.status_code != 200:
            return {"error": "Invalid symbol or data unavailable"}
        
        # Parsing logic needs to be implemented based on Google's response
        return {"error": "Google Finance parsing not implemented"}