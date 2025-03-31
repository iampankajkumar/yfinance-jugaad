from datetime import datetime
from nsepython import nse_eq

from service.stock_price_provider import AbstractStockPriceProvider

class NSEPythonPriceProvider(AbstractStockPriceProvider):
    def get_ohlc(self, symbol):
        data = nse_eq(symbol)
        
        if not data:
            raise ValueError("Invalid symbol or data unavailable = {}",symbol)
        
        last_update_time = data['metadata']['lastUpdateTime']
        formatted_date = datetime.strptime(last_update_time, "%d-%b-%Y %H:%M:%S").strftime("%Y-%m-%d 00:00:00.000")
        
        return {
            "recordDate": formatted_date,
            "open": round(float(data['priceInfo']['open']), 2),
            "high": round(float(data['priceInfo']['intraDayHighLow']['max']), 2),
            "low": round(float(data['priceInfo']['intraDayHighLow']['min']), 2),
            "close": round(float(data['priceInfo']['close']), 2),
            "ltp": round(float(data['priceInfo']['lastPrice']), 2),
            "volume": int(data.get('preOpenMarket', {}).get('totalTradedVolume', 0))
        }