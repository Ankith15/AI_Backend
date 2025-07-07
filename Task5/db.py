import mysql.connector
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

DB_NAME = os.getenv("MYSQL_DB", "binance_prices")
DB_USER = os.getenv("MYSQL_USER", "root")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
DB_HOST = os.getenv("MYSQL_HOST", "localhost")
DB_PORT = int(os.getenv("MYSQL_PORT", "3306"))

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

def insert_price(timestamp: datetime, symbol: str, price: float):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO prices (timestamp, symbol, price)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], symbol, price))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ DB Insert Error: {e}")
