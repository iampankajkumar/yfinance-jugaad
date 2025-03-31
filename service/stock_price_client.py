from factory.stock_price_factory import StockPriceDataFactory


class StockPriceDataClient:
    def __init__(self, provider_name):
        self.provider = StockPriceDataFactory.get_provider(provider_name)
        if not self.provider:
            raise ValueError(f"Invalid provider: {provider_name}")

    def fetch_ohlc(self, symbol):
        return self.provider.get_ohlc(symbol)
