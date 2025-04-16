from datetime import datetime
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine, text
from constants.ticker_name_map import Tickers
import redis
from io import StringIO


# Database connection
db_params = {
    "host": "localhost",
    "port": "5444",
    "database": "equity_stream",
    "user": "tkcsowner",
    "password": "tkcsowner"
}

engine = create_engine(f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")

# Prepare SQL insert/update query
insert_query = text('''
    INSERT INTO prices (record_date, key, name, current_price, daily_volume, low_price, created_at, updated_at)
    VALUES (:record_date, :key, :name, :current_price, :daily_volume, :low_price, :created_at, :updated_at)
    ON CONFLICT (key, record_date)
    DO UPDATE 
    SET 
        current_price = EXCLUDED.current_price,
        daily_volume = EXCLUDED.daily_volume,
        low_price = EXCLUDED.low_price,
        updated_at = EXCLUDED.updated_at;
''')

# Connect to Redis (adjust if using Upstash or remote Redis)
r = redis.Redis(host='gusc1-cool-owl-30106.upstash.io', port=30106, password='0d7dbff6f4a54d10b9956ac9cf8a5215', ssl=True, decode_responses=True)

# Today's date for cache key
today_str = datetime.today().strftime("%Y-%m-%d")

# Fetch and insert data for each ticker
for ticker_symbol, name in Tickers().ticker_json.items():
    try:
        redis_key = f"history:{ticker_symbol}:{today_str}"

        # Check cache first
        cached = r.get(redis_key)
        if cached:
            print(f"✅ Using cached data for {redis_key}")
            data = pd.read_json(StringIO(cached), convert_dates=True)
        else:
            print(f"📡 Fetching data from API for {redis_key}")
            ticker = yf.Ticker(ticker_symbol)
            data = ticker.history(period="5d", interval="1d")

            if data.empty:
                print(f"⚠️ No data available for {ticker_symbol}")
                continue

            # Cache the data in Redis
            r.set(redis_key, data.to_json(), ex=86400)  # Optional: expire after 1 day

        with engine.connect() as conn:
            for index, row in data.iterrows():
                record_date = str(index).split('+')[0]
                conn.execute(insert_query, {
                    'record_date': datetime.strptime(record_date, "%Y-%m-%d %H:%M:%S"),
                    'key': ticker_symbol,
                    'name': name,
                    'current_price': round(float(row['Close']), 2) if pd.notnull(row['Close']) else None,
                    'daily_volume': int(row['Volume']) if pd.notnull(row['Volume']) else None,
                    'low_price': round(float(row['Low']), 2) if pd.notnull(row['Low']) else None,
                    'created_at': datetime.now(),
                    'updated_at': datetime.now()
                })
            conn.commit()
        print(f"✅ Data inserted/updated for {ticker_symbol}")

    except Exception as e:
        print(f"❌ Error with {ticker_symbol}: {e}")

print("🎉 Data processing complete!")