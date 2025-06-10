from nsepython import *

# Get quote
quote = nse_quote("RELIANCE")
print(quote['lastPrice'])

# Historical data
history = nse_fetch_chart_data("RELIANCE", "1d", "1mo")
print(history)
