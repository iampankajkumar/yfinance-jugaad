from impl.alphavintage_price_provider import AlphaVantagePriceProvider
from impl.google_finance_price_provider import GoogleFinancePriceProvider
from impl.nse_python_price_provider import NSEPythonPriceProvider
from impl.yfinance_price_provider import YahooFinanceProvider


class StockPriceDataFactory:
    providers = {
        "nse": NSEPythonPriceProvider(),
        "yahoo": YahooFinanceProvider(),
        "alphavantage": AlphaVantagePriceProvider(),
        "google": GoogleFinancePriceProvider(),
    }
    
    @staticmethod
    def get_provider(source):
        return StockPriceDataFactory.providers.get(source, None)
