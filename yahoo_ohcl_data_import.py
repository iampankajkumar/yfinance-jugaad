from datetime import datetime
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine, text
from constants.ticker_name_map import Tickers

# Database connection
db_params = {
    "host": "localhost",
    "port": "5444",
    "database": "equity_stream",
    "user": "tkcsowner",
    "password": "tkcsowner"
}

engine = create_engine(f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")

# List of ticker symbols
# ticker_symbols = Tickers().ticker_json.keys

# Prepare SQL insert/update query
# insert_query = text('''
#     INSERT INTO prices (record_date, key, name, current_price, daily_volume, created_at, updated_at)
#     VALUES (:record_date, :key, :name, :current_price, :daily_volume, :created_at, :updated_at)
#     ON CONFLICT (key, record_date)
#     DO UPDATE SET
#         current_price = EXCLUDED.current_price,
#         updated_at = EXCLUDED.updated_at;
# ''')

insert_query = text('''
    INSERT INTO prices (record_date, key, name, current_price, daily_volume, created_at, updated_at)
    VALUES (:record_date, :key, :name, :current_price, :daily_volume, :created_at, :updated_at)
    ON CONFLICT (key, record_date)
    DO UPDATE 
    SET 
        current_price = EXCLUDED.current_price,
        daily_volume = EXCLUDED.daily_volume,
        updated_at = EXCLUDED.updated_at;
''')

# Fetch and insert data for each ticker
for  ticker_symbol, name in Tickers().ticker_json.items():
    try:
        ticker = yf.Ticker(ticker_symbol)
        data = ticker.history(period="5d", interval="1d")

        if data.empty:
            print(f"No data available for {ticker_symbol}")
            continue

        with engine.connect() as conn:
            for index, row in data.iterrows():
                record_date = str(index).split('+')[0]
                conn.execute(insert_query, {
                    'record_date': datetime.strptime(record_date, "%Y-%m-%d %H:%M:%S"),
                    'key': ticker_symbol,
                    'name': ticker.info.get('shortName', 'Unknown'),
                    'current_price': round(float(row['Close']), 2) if pd.notnull(row['Close']) else None,
                    'daily_volume': int(row['Volume']) if pd.notnull(row['Volume']) else None,
                    'created_at': datetime.now(),
                    'updated_at': datetime.now()
                })
            conn.commit()
        print(f"Data inserted/updated successfully for {ticker_symbol}!")

    except Exception as e:
        print(f"An error occurred with {ticker_symbol}: {e}")

print("Data processing complete!")

# Let me know if you want any adjustments! 🚀
