from flask import Flask, render_template
import pandas as pd
from ticker_name_map import Tickers
import yfinance as yf
import pandas_ta as ta
from datetime import datetime
import os
import pickle
from db_handler import DBHandler

app = Flask(__name__)

# Initialize Database Singleton
db_handler = DBHandler()

# Function to calculate current RSI
def calculate_current_rsi(data, period):
    if len(data) < period:
        return None
    rsi = ta.rsi(data['Close'], length=period)
    if rsi.isna().all():
        return None
    return rsi.iloc[-1]

# Directory to store daily data
DATA_DIR = 'daily_data'

# Generate filename based on current date and ticker name
def generate_filename(ticker):
    today = datetime.today().strftime('%Y_%m_%d')
    filename = f"{today}_{ticker}.pkl"
    return os.path.join(DATA_DIR, filename)

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
def fetch_stock_data(ticker, interval):
    # Ensure the directory exists
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    # Clean up old files
    cleanup_old_files(DATA_DIR)
    
    filename = generate_filename(ticker)
    
    # Check if file exists
    if os.path.exists(filename):
        # Load data from file
        with open(filename, 'rb') as file:
            stock_data = pickle.load(file)
    else:
        # Download data and save to file
        stock_data = yf.download(ticker, period="2y", interval=interval)
        with open(filename, 'wb') as file:
            pickle.dump(stock_data, file)
    
    return stock_data

# Function to calculate all-time high
def calculate_all_time_high(data):
    if data.empty:
        return None
    return data['Close'].max()

# Function to calculate returns
def calculate_returns(data):
    return_data = {key: None for key in ['1dReturn', '1wReturn', '1mReturn', '6mReturn', '1yReturn', '2yReturn']}
    if len(data) < 2:
        return return_data

    latest_price = data['Close'].iloc[-1]
    
    if len(data) > 1:
        return_data['1dReturn'] = ((latest_price - data['Close'].iloc[-2]) / data['Close'].iloc[-2]) * 100

    if len(data) > 8:
        return_data['1wReturn'] = ((latest_price - data['Close'].iloc[-8]) / data['Close'].iloc[-8]) * 100

    if len(data) > 22:
        return_data['1mReturn'] = ((latest_price - data['Close'].iloc[-22]) / data['Close'].iloc[-22]) * 100

    if len(data) > 126:
        return_data['6mReturn'] = ((latest_price - data['Close'].iloc[-126]) / data['Close'].iloc[-126]) * 100

    if len(data) > 252:
        return_data['1yReturn'] = ((latest_price - data['Close'].iloc[-252]) / data['Close'].iloc[-252]) * 100

    if len(data) > 0:
        return_data['2yReturn'] = ((latest_price - data['Close'].iloc[0]) / data['Close'].iloc[0]) * 100
    
    return return_data

# Function to generate fund data and store it in the database
def generate_fund_data(ticker_name_map):
    funds_data = []
    for ticker, name in ticker_name_map.items():
        try:
            daily_data = fetch_stock_data(ticker, '1d')
            daily_data.reset_index(inplace=True)  # Add this line
            
            current_rsi_daily = calculate_current_rsi(daily_data, 14)

            # Set Date as DatetimeIndex
            daily_data['Date'] = pd.to_datetime(daily_data['Date'])
            daily_data.set_index('Date', inplace=True)

            weekly_data = daily_data.resample('W').last()
            current_rsi_weekly = calculate_current_rsi(weekly_data, 14)

            monthly_data = daily_data.resample('M').last()
            current_rsi_monthly = calculate_current_rsi(monthly_data, 14)

            all_time_high = calculate_all_time_high(daily_data)
            nav = daily_data['Close'].iloc[-1] if not daily_data.empty else None
            discount = ((all_time_high - nav) / all_time_high * 100) if all_time_high and nav else None
            
            returns = calculate_returns(daily_data)

            fund_entry = {
                "key": ticker,
                "name": name,
                "recordDate": daily_data.index[-1], 
                "nav": round(nav, 2) if nav else None,
                "1dRSI": round(current_rsi_daily, 1) if current_rsi_daily is not None else None,
                "1wRSI": round(current_rsi_weekly, 1) if current_rsi_weekly is not None else None,
                "1mRSI": round(current_rsi_monthly, 1) if current_rsi_monthly is not None else None,
                "allTimeHigh": round(all_time_high, 2) if all_time_high else None,
                "discount": round(discount, 2) if discount else None,
                "1dReturn": round(returns['1dReturn'], 2) if returns['1dReturn'] is not None else None,
                "1wReturn": round(returns['1wReturn'], 2) if returns['1wReturn'] is not None else None,
                "1mReturn": round(returns['1mReturn'], 2) if returns['1mReturn'] is not None else None,
                "6mReturn": round(returns['6mReturn'], 2) if returns['6mReturn'] is not None else None,
                "1yReturn": round(returns['1yReturn'], 2) if returns['1yReturn'] is not None else None,
                "2yReturn": round(returns['2yReturn'], 2) if returns['2yReturn'] is not None else None,
                "Volume": daily_data['Volume'].iloc[-1] if not daily_data.empty else None
            }
            funds_data.append(fund_entry)
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
    
    # Store data in the database
    db_handler.insert_fund_data(funds_data)
    return funds_data

# Main function
def main():
    ticker_name_map = Tickers().ticker_json
    return generate_fund_data(ticker_name_map)

# Fetch and store data
data = main()

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
