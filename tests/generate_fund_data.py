import json  # Import the json module
import yfinance as yf
import pandas_ta as ta
from datetime import datetime

# Function to calculate current RSI
def calculate_current_rsi(data, period):
    if len(data) < period:
        return None
    rsi = ta.rsi(data['Close'], length=period)
    if rsi.isna().all():
        return None
    return rsi.iloc[-1]

# Fetch stock data from Yahoo Finance
def fetch_stock_data(ticker, interval):
    stock_data = yf.download(ticker, period="2y", interval=interval)
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
        return return_data  # Not enough data for any returns

    latest_price = data['Close'].iloc[-1]
    
    # Calculate 1-day return
    if len(data) > 1:  # Ensure there are at least 2 data points
        return_data['1dReturn'] = ((latest_price - data['Close'].iloc[-2]) / data['Close'].iloc[-2]) * 100

    # Calculate 1-week return
    if len(data) > 8:  # At least 8 data points for a week
        return_data['1wReturn'] = ((latest_price - data['Close'].iloc[-8]) / data['Close'].iloc[-8]) * 100

    # Calculate 1-month return
    if len(data) > 22:  # At least 22 data points for a month
        return_data['1mReturn'] = ((latest_price - data['Close'].iloc[-22]) / data['Close'].iloc[-22]) * 100

    # Calculate 6-month return
    if len(data) > 126:  # At least 126 data points for 6 months
        return_data['6mReturn'] = ((latest_price - data['Close'].iloc[-126]) / data['Close'].iloc[-126]) * 100

    # Calculate 1-year return
    if len(data) > 252:  # At least 252 data points for 1 year
        return_data['1yReturn'] = ((latest_price - data['Close'].iloc[-252]) / data['Close'].iloc[-252]) * 100

    # Calculate 2-year return
    if len(data) > 0:  # There should be at least 1 data point for 2 years
        return_data['2yReturn'] = ((latest_price - data['Close'].iloc[0]) / data['Close'].iloc[0]) * 100
    
    return return_data

# Function to generate fund data
def generate_fund_data(ticker_name_map):
    funds_data = []
    for ticker, name in ticker_name_map.items():
        # Fetch daily stock data
        daily_data = fetch_stock_data(ticker, '1d')
        current_rsi_daily = calculate_current_rsi(daily_data, 14)

        # Calculate weekly and monthly RSI
        weekly_data = daily_data.resample('W').last()
        current_rsi_weekly = calculate_current_rsi(weekly_data, 14)

        monthly_data = daily_data.resample('M').last()
        current_rsi_monthly = calculate_current_rsi(monthly_data, 14)

        # Calculate all-time high and discount
        all_time_high = calculate_all_time_high(daily_data)
        nav = daily_data['Close'].iloc[-1] if not daily_data.empty else None
        discount = ((all_time_high - nav) / all_time_high * 100) if all_time_high and nav else None
        
        # Calculate returns
        returns = calculate_returns(daily_data)

        # Construct fund data entry
        fund_entry = {
            "key": ticker,
            "name": name,
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
            "updatedOn": datetime.now().strftime("%Y-%m-%d")
        }
        funds_data.append(fund_entry)

    return funds_data

# Main function to generate the JSON-like structure
def main():
    ticker_name_map = {
        "0P0000XW51.BO": "Quant ELSS Tax Saver Fund",
        "0P00017844.BO": "Mirae Asset ELSS Tax Saver Fund",
        "0P00005VCS.BO": "HSBC ELSS Tax Saver Fund",
        "0P0000XVU7.BO": "Axis ELSS Tax Saver Fund",
        "0P0000XV1I.BO": "Bandhan ELSS Tax Saver Fund",
        "0P0001R64W.BO": "Motilal Oswal Nifty Microcap 250 Index Fund",
        "0P0000XVDP.BO": "Nippon India Growth Direct Growth",
        "0P0001RQX5.BO": "Zerodha Nifty LargeMidcap 250 Index Fund Tax Saver Dir Gr",
        "0P0000GB29.BO": "Aditya BSL ELSS Tax Saver Gr",
        "0P0000XW04.BO": "Canara Robeco ELSS Tax Saver Dir Gr",
        "0P00011MAX.BO": "Axis Small Cap Fund Dir Gr",
        "RELIANCE.NS": "Reliance Industries Ltd",
        "ASTRAL.NS": "Astral Poly Technik Ltd",
        "AUTOBEES.NS": "Nippon India ETF Nifty Auto",
        "AUTOIETF.NS": "Aditya Birla Sun Life ETF Nifty Auto",
    }
    
    # Generate fund data and print as JSON
    fund_data = generate_fund_data(ticker_name_map)
    print(json.dumps(fund_data, indent=0))  # Use indent for pretty-printing


if __name__ == "__main__":
    main()
