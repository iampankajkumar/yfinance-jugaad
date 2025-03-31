from abc import ABC, abstractmethod

class AbstractStockPriceProvider(ABC):
    """Abstract Base Class for stock data providers."""
    
    @abstractmethod
    def get_ohlc(self, symbol):
        pass
