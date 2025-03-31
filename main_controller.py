from flask import Flask, render_template
import pandas as pd
import psycopg2
from constants.ticker_name_map import Tickers
import yfinance as yf
import pandas_ta as ta
from datetime import datetime
import os
import pickle
from dbhandler.db_handler import DBHandler
from sqlalchemy import create_engine
import pandas as pd
import diskcache as dc
import yfinance as yf
import pandas as pd
import pandas_ta as ta
from flask import Flask, render_template
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import numpy as np
import pandas_ta as ta

app = Flask(__name__)

# Initialize Database Singleton
db_handler = DBHandler()


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

    
# Function to calculate current RSI
def calculate_current_rsi(data, period):
    if data.empty or 'Close' not in data.columns:
        print("RSI calculation failed: Data empty or missing 'Close' column.")
        return 50  # Default RSI value when data is missing
    
    rsi = ta.rsi(data['Close'], length=period)
    
    if rsi is None or rsi.isna().all():
        print("RSI calculation failed: RSI contains only NaN values.")
        return 50  # Default RSI value when RSI cannot be calculated
    
    return rsi.dropna().iloc[-1]

# Directory to store daily data
DATA_DIR = 'daily_data'

# Generate filename based on current date and ticker name
def generate_filename(ticker):
    today = datetime.today().strftime('%Y_%m_%d')
    return os.path.join(DATA_DIR, f"{today}_{ticker}.pkl")

# Clean up old files in the directory, but keep current day's files
def cleanup_old_files(directory):
    today = datetime.today().strftime('%Y_%m_%d')
    for filename in os.listdir(directory):
        if today in filename:
            continue
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

# Fetch stock data from Yahoo Finance
# def fetch_stock_data(ticker, interval):
#     os.makedirs(DATA_DIR, exist_ok=True)
#     cleanup_old_files(DATA_DIR)
#     filename = generate_filename(ticker)
#     if os.path.exists(filename):
#         try:
#             with open(filename, 'rb') as file:
#                 stock_data = pickle.load(file)
#                 if not stock_data.empty:
#                     return stock_data
#         except Exception as e:
#             print(f"Error loading {filename}: {e}")
#     stock_data = yf.download(ticker, period="2y", interval=interval, auto_adjust=True, progress=False)
#     with open(filename, 'wb') as file:
#         pickle.dump(stock_data, file)
#     print(stock_data)
#     return stock_data


DB_CONFIG = {
    "host": "localhost",
    "port": "5444",
    "database": "equity_stream",
    "user": "tkcsowner",
    "password": "tkcsowner"
}

# Create SQLAlchemy engine
engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

# Cache settings with diskcache
CACHE_DIR = 'stock_data_cache'
cache = dc.Cache(CACHE_DIR)


def fetch_stock_data(ticker, interval):
    try:
        today_str = datetime.now().strftime('%Y-%m-%d')
        cache_key = f"{ticker}_{interval}_{today_str}"

        # Check cache first
        if cache_key in cache:
            print(f"Serving data from cache for {ticker} on {today_str}")
            return cache[cache_key]

        print(f"Fetching data for ticker: {ticker}, interval: {interval}")

        query = """
            SELECT record_date AS "Date", current_price as "Close", daily_volume as "Volume"
            FROM public.prices
            WHERE key = %s
            ORDER BY record_date DESC
        """
        
        # Load data into a DataFrame
        df = pd.read_sql_query(query, engine, params=(ticker,))

        if df.empty:
            print(f"No data found for ticker {ticker} on {today_str}.")
            return pd.DataFrame()

        # Convert Date to datetime and set as index
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df.dropna(subset=['Date'], inplace=True)
        df.set_index('Date', inplace=True)

        if df.index.isnull().any():
            print(f"Warning: Null values found in index after conversion for {ticker}")

        # Downcast numeric columns to save memory
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce', downcast='float')
        df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce', downcast='integer')
    
        # Resample data based on the interval
        if interval == '1d':
            df = df.resample('D').last().dropna()

        # Cache the result with a 24-hour expiry
        cache.set(cache_key, df, expire=24 * 60 * 60)
        print(f"Cached data for {ticker} on {today_str} with a 24-hour expiry.")

        return df

    except Exception as e:
        print(f"Error fetching data from PostgreSQL: {e}")
        return pd.DataFrame()

# Function to calculate all-time high
def calculate_all_time_high(data):
    return None if data.empty else data['Close'].max()

# Function to calculate returns
def calculate_returns(data):
    return_data = {key: None for key in ['1dReturn', '1wReturn', '1mReturn', '6mReturn', '1yReturn', '2yReturn', '3yReturn']}
    if len(data) < 2:
        return return_data
    latest_price = data['Close'].iloc[-1]
    periods = {'1d': 1, '1w': 8, '1m': 22, '6m': 126, '1y': 252, '2y': 252*2, '3y': 252*3}
    for key, days in periods.items():
        if len(data) > days:
            return_data[f"{key}Return"] = ((latest_price - data['Close'].iloc[-days]) / data['Close'].iloc[-days]) * 100
    return return_data

# Generate fund data and store it in the database
def generate_fund_data(ticker_name_map):
    funds_data = []
    for ticker, name in ticker_name_map.items():
        try:
            daily_data = fetch_stock_data(ticker, '1d')

            if daily_data.empty:
                raise ValueError(f"No data available for ticker {ticker}")

            daily_data.reset_index(inplace=True)
            daily_data['Date'] = pd.to_datetime(daily_data['Date'])
            daily_data.set_index('Date', inplace=True)

            current_rsi_daily = calculate_current_rsi(daily_data, 14)
            weekly_data = daily_data.resample('W').last()
            current_rsi_weekly = calculate_current_rsi(weekly_data, 14)
            monthly_data = daily_data.resample('ME').last()
            current_rsi_monthly = calculate_current_rsi(monthly_data, 14)

            all_time_high = calculate_all_time_high(daily_data)
            nav = daily_data['Close'].iloc[-1] if not daily_data.empty else None
            discount = ((all_time_high - nav) / all_time_high * 100) if all_time_high and nav else None

            returns = calculate_returns(daily_data)
            strength = calculate_stock_strength(ticker)
            fund_entry = {
                "key": ticker,
                "name": name,
                "recordDate": daily_data.index[-1].strftime("%Y-%m-%d 00:00:00.000") if not daily_data.empty else None,
                "nav": round(nav, 2) if nav else None,
                "1dRSI": round(current_rsi_daily, 1),
                "strengthScore":strength['strength_score'],
                "strengthLabel":strength['strength_label'], 
                "1wRSI": round(current_rsi_weekly, 1),
                "1mRSI": round(current_rsi_monthly, 1),
                "allTimeHigh": round(all_time_high, 2) if all_time_high else None,
                "discount": round(discount, 2) if discount else None,
                "1dReturn": round(returns['1dReturn'], 2) if returns['1dReturn'] is not None else None,
                "1wReturn": round(returns['1wReturn'], 2) if returns['1wReturn'] is not None else None,
                "1mReturn": round(returns['1mReturn'], 2) if returns['1mReturn'] is not None else None,
                "6mReturn": round(returns['6mReturn'], 2) if returns['6mReturn'] is not None else None,
                "1yReturn": round(returns['1yReturn'], 2) if returns['1yReturn'] is not None else None,
                "2yReturn": round(returns['2yReturn'], 2) if returns['2yReturn'] is not None else None,
                "3yReturn": round(returns['3yReturn'], 2) if returns['3yReturn'] is not None else None,
                "Volume": int(daily_data['Volume'].iloc[-1]) if not pd.isnull(daily_data['Volume'].iloc[-1]) else 0
            }
            funds_data.append(fund_entry)

        except Exception as e:
            print(f"Error processing {ticker}: {e}")

    # db_handler.insert_fund_data(funds_data)
    return funds_data

# Create a session from the existing engine
Session = sessionmaker(bind=engine)
session = Session()

# SQL query to fetch stock price data
query = text("""
            SELECT 
                p.key,
                json_agg(
                    json_build_object(
                        'year', p.year,
                        'lowest_price', p.lowest_price,
                        'highest_price', p.highest_price
                    ) ORDER BY p.year DESC -- Sort years inside the JSON array
                ) AS price_data,
                cp.current_price
            FROM (
                SELECT 
                    key,
                    EXTRACT(YEAR FROM record_date) AS year,
                    MIN(current_price) AS lowest_price,
                    MAX(current_price) AS highest_price
                FROM 
                    prices
                GROUP BY 
                    key, EXTRACT(YEAR FROM record_date)
            ) p
            LEFT JOIN (
                SELECT DISTINCT ON (key) 
                    key,
                    current_price AS current_price
                FROM 
                    prices
                ORDER BY 
                    key, record_date DESC  -- Fix: key must be the first column in ORDER BY
            ) cp ON p.key = cp.key
            GROUP BY 
                p.key, cp.current_price
            ORDER BY 
                p.key;  -- Order by stock key only
        """)


def fetch_stock_data_2():
    try:
        result = session.execute(query)
        stocks = []
        
        for row in result:
            stocks.append({
                "key": row[0],
                "price_data": row[1],
                "current_price": row[2]  # Add current price from query
            })
        return stocks
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Main function
def main():
    ticker_name_map = Tickers().ticker_json
    return generate_fund_data(ticker_name_map)

# Fetch and store data
data = main()

@app.route('/')
def index():
    return render_template('index.html', data=data)

# Stock price summary page
@app.route('/stocks')
def stock_prices():
    stocks = fetch_stock_data_2()
    return render_template('stock_prices.html', stocks=stocks)

@app.route('/tickers')
def load_tickers():
    return render_template('tickers.html')

@app.route('/api/tickers', methods=['GET'])
def get_tickers():
    result = session.execute(text("SELECT * FROM tickers"))
    tickers = [dict(row._mapping) for row in result]
    return jsonify(tickers)

@app.route('/api/tickers', methods=['POST'])
def add_ticker():
    data = request.json
    try:
        session.execute(
            text("INSERT INTO tickers (key, name, type, yahoo_key) VALUES (:key, :name, :type, :yahoo_key)")
            .bindparams(**data)
        )
        session.commit()
        return jsonify({"message": "Ticker added successfully"}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/tickers/<string:key>', methods=['PUT'])
def update_ticker(key):
    data = request.json
    try:
        session.execute(
            text("UPDATE tickers SET name = :name, type = :type, yahoo_key = :yahoo_key WHERE key = :key")
            .bindparams(**data, key=key)
        )
        session.commit()
        return jsonify({"message": "Ticker updated successfully"})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/tickers/<string:key>', methods=['DELETE'])
def delete_ticker(key):
    try:
        session.execute(text("DELETE FROM tickers WHERE key = :key").bindparams(key=key))
        session.commit()
        return jsonify({"message": "Ticker deleted successfully"})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
