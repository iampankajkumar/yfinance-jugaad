import random
from service.stock_price_client import StockPriceDataClient


SYMBOL_MAPPING = {
    "nse": "{symbol}",                # No suffix for NSE
    "yahoo": "{symbol}.NS",           # Add .NS for Yahoo
    "alphavantage": "{symbol}.BSE",   # Add .BSE for Alpha Vantage
    # "google": "{symbol}",           # Example for future providers
}

def fetch_with_retry(symbol, clients):
    remaining_clients = clients[:]

    while remaining_clients:
        client_name = random.choice(remaining_clients)
        try:
            client = StockPriceDataClient(client_name)
            
            # Format the symbol based on the provider
            formatted_symbol = SYMBOL_MAPPING.get(client_name, "{symbol}").format(symbol=symbol)
            
            result = client.fetch_ohlc(formatted_symbol)
            return result
        except Exception as e:
            print(f"Error with {client_name}: {e}")
            remaining_clients.remove(client_name)
    
    raise Exception("All implementations failed!")


if __name__ == "__main__":
    implementations = ["nse", "yahoo", "alphavantage"]
    symbol = "MON100"

    try:
        ohlc_data = fetch_with_retry(symbol, implementations)
        print(ohlc_data)
    except Exception as e:
        print(f"Final failure: {e}")

    # You can add more implementations later, like:
    # implementations.append("google")
