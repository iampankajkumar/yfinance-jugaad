import yfinance as yf
import pandas as pd
import pandas_ta as ta


import numpy as np
import pandas_ta as ta

print(np.__version__)
print(ta.__version__)

def calculate_stock_strength(ticker, period='1y'):
    # Fetch historical data
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)

    if df.empty:
        raise ValueError("No data found for ticker: {}".format(ticker))

    # Calculate technical indicators using pandas_ta
    df['50_MA'] = df['Close'].rolling(window=50).mean()
    df['200_MA'] = df['Close'].rolling(window=200).mean()
    df['RSI'] = ta.rsi(df['Close'], length=14)
    macd = ta.macd(df['Close'])
    df['MACD'] = macd['MACD_12_26_9']
    df['MACD_signal'] = macd['MACDs_12_26_9']
    df['Volume_MA'] = df['Volume'].rolling(window=20).mean()

    # Latest data points
    latest = df.iloc[-1]

    # Scoring logic
    score = 0
    if latest['50_MA'] > latest['200_MA']:
        score += 20  # Bullish crossover
    if latest['RSI'] < 30:
        score -= 10  # Oversold
    elif latest['RSI'] > 70:
        score += 10  # Overbought momentum
    if latest['MACD'] > latest['MACD_signal']:
        score += 20  # Positive MACD crossover
    if latest['Volume'] > latest['Volume_MA']:
        score += 10  # Increasing volume

    # Normalize score
    strength = min(max(score, 0), 100)

    # Classify stock strength
    if strength <= 25:
        strength_label = "Very Weak"
    elif strength <= 50:
        strength_label = "Weak"
    elif strength <= 75:
        strength_label = "Strong"
    else:
        strength_label = "Very Strong"

    return {
        'ticker': ticker,
        'strength_score': strength,
        'strength_label': strength_label,
        'latest_price': latest['Close'],
        '50_MA': latest['50_MA'],
        '200_MA': latest['200_MA'],
        'RSI': latest['RSI'],
        'MACD': latest['MACD'],
        'Volume': latest['Volume']
    }

# Example usage
ticker = 'AAPL'
result = calculate_stock_strength(ticker)
print(result)
