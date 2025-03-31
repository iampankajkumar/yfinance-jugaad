import yfinance as yf

ticker = yf.Ticker("TCS.NS")
print(ticker.financials.index)
