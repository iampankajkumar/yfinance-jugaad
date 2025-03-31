import psycopg2
import numpy as np
from psycopg2.extensions import register_adapter, AsIs

# Automatically adapt numpy types to PostgreSQL
register_adapter(np.int64, AsIs)
register_adapter(np.float64, AsIs)

class DBHandler:
    _instance = None  # Singleton pattern

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DBHandler, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'connection'):
            self.dbname = "equity_stream"
            self.user = "tkcsowner"
            self.password = "tkcsowner"
            self.host = "localhost"
            self.port = "5444"
            self.connection = self.connect_to_db()
            self.cursor = self.connection.cursor()

    def connect_to_db(self):
        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Database connection established.")
            return conn
        except Exception as e:
            print(f"Database connection error: {e}")
            raise

    def insert_fund_data(self, data_list):
        insert_query = """
        INSERT INTO prices (
            record_date, key, name, current_price, ath, discount_percent,
            rsi_1d, rsi_1w, rsi_1m,
            return_1d, return_1w, return_1m, return_6m,
            return_1y, return_2y, daily_volume, created_at, updated_at
        ) VALUES (
            %(recordDate)s, %(key)s, %(name)s, %(nav)s, %(allTimeHigh)s, %(discount)s,
            %(1dRSI)s, %(1wRSI)s, %(1mRSI)s,
            %(1dReturn)s, %(1wReturn)s, %(1mReturn)s, %(6mReturn)s,
            %(1yReturn)s, %(2yReturn)s, %(Volume)s,
            CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
        )
        ON CONFLICT (key, record_date)
        DO UPDATE SET
            current_price = EXCLUDED.current_price,
            ath = EXCLUDED.ath,
            discount_percent = EXCLUDED.discount_percent,
            rsi_1d = EXCLUDED.rsi_1d,
            rsi_1w = EXCLUDED.rsi_1w,
            rsi_1m = EXCLUDED.rsi_1m,
            return_1d = EXCLUDED.return_1d,
            return_1w = EXCLUDED.return_1w,
            return_1m = EXCLUDED.return_1m,
            return_6m = EXCLUDED.return_6m,
            return_1y = EXCLUDED.return_1y,
            return_2y = EXCLUDED.return_2y,
            daily_volume = EXCLUDED.daily_volume,
            updated_at = CURRENT_TIMESTAMP
        RETURNING xmax;
        """
        try:
            insert_count = 0
            update_count = 0
            for fund in data_list:
                # Convert numpy types to native Python types
                fund = {k: (v.item() if isinstance(v, (np.int64, np.float64)) else v) for k, v in fund.items()}

                self.cursor.execute(insert_query, fund)
                result = self.cursor.fetchone()

                if result and result[0] == 0:
                    insert_count += 1
                else:
                    update_count += 1

            self.connection.commit()
            print(f"Inserted: {insert_count}, Updated: {update_count} records.")
        except Exception as e:
            print(f"Error inserting data: {e}")
            self.connection.rollback()
