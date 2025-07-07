from db import get_connection
from datetime import datetime, timedelta, timezone

def get_latest_price(symbol: str):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT price, timestamp FROM prices
        WHERE symbol = %s
        ORDER BY timestamp DESC
        LIMIT 1
    """
    cursor.execute(query, (symbol,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_price_at(symbol: str, target_time: datetime):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT price, timestamp FROM prices
        WHERE symbol = %s AND DATE_FORMAT(timestamp, '%%Y-%%m-%%d %%H:%%i:%%s') = DATE_FORMAT(%s, '%%Y-%%m-%%d %%H:%%i:%%s')
        ORDER BY timestamp DESC
        LIMIT 1
    """
    cursor.execute(query, (symbol, target_time))
    result = cursor.fetchone()
    conn.close()
    return result

def get_min_max_in_interval(symbol: str, start: datetime, end: datetime):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT MIN(price), MAX(price) FROM prices
        WHERE symbol = %s AND timestamp BETWEEN %s AND %s
    """
    cursor.execute(query, (symbol, start, end))
    result = cursor.fetchone()
    conn.close()
    return result

if __name__ == "__main__":
    symbol = "BTCUSDT"

    print("🔍 Latest Price:")
    print(get_latest_price(symbol))

    # Using current UTC time and recent time range
    now = datetime.now(timezone.utc)
    test_time = now - timedelta(seconds=5)

    print("\n⏱ Price at specific time:")
    print(get_price_at(symbol, test_time))

    print("\n📊 Min/Max in last 1 minute:")
    one_min_ago = now - timedelta(minutes=5)
    print(get_min_max_in_interval(symbol, one_min_ago, now))
