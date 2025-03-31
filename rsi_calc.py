import pandas as pd
import pandas_ta as ta
import psycopg2
from sqlalchemy import create_engine

# Database connection details
DB_NAME = "equity_stream"
DB_USER = "tkcsowner"
DB_PASSWORD = "tkcsowner"
DB_HOST = "localhost"
DB_PORT = "5444"

# Connect to PostgreSQL
def get_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

from sqlalchemy import create_engine

def fetch_prices():
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    query = "SELECT key, record_date, current_price FROM prices;"
    df = pd.read_sql_query(query, engine)
    engine.dispose()
    return df

# Calculate RSI
def calculate_rsi(df, period=14):
    df['RSI'] = ta.rsi(df['current_price'], length=period)
    return df

def calculate_weekly_rsi(df, period=14):
    df.set_index('record_date', inplace=True)
    weekly_prices = df['current_price'].resample('W').last()
    weekly_rsi = ta.rsi(weekly_prices, length=period)
    
    if weekly_rsi is not None:
        df['RSI_weekly'] = weekly_rsi.reindex(df.index, method='ffill')
    else:
        df['RSI_weekly'] = None
    
    return df.reset_index()


def calculate_monthly_rsi(df, period=14):
    df.set_index('record_date', inplace=True)
    monthly_prices = df['current_price'].resample('M').last()
    monthly_rsi = ta.rsi(monthly_prices, length=period)
    df['RSI_monthly'] = monthly_rsi.reindex(df.index, method='ffill')
    return df.reset_index()

# Save RSI results to the database
def save_to_database(df):
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    create_table_query = """
    CREATE TABLE IF NOT EXISTS ticker_summary (
        key VARCHAR(20) NOT NULL,
        record_date TIMESTAMP NOT NULL,
        current_price NUMERIC(10, 2),
        RSI NUMERIC(10, 2),
        RSI_weekly NUMERIC(10, 2),
        RSI_monthly NUMERIC(10, 2),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (key, record_date)
    );
    """
    with engine.connect() as conn:
        conn.execute(create_table_query)

    # Insert or update data
    df.to_sql('ticker_summary', engine, if_exists='replace', index=False)

# Main function
def main():
    df = fetch_prices()
    if df.empty:
        print("No data found!")
        return

    df['record_date'] = pd.to_datetime(df['record_date'])
    df = df.sort_values(by=['key', 'record_date'])

    df = df.groupby('key', group_keys=False).apply(calculate_rsi)
    df = df.groupby('key', group_keys=False).apply(calculate_weekly_rsi)
    df = df.groupby('key', group_keys=False).apply(calculate_monthly_rsi)

    df = df.dropna(subset=['RSI'])
    save_to_database(df)
    print("RSI data calculated and saved!")

if __name__ == "__main__":
    main()
