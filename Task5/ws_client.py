import asyncio
import websockets
import json
from datetime import datetime, timezone
from db import insert_price

SYMBOLS = ["btcusdt", "ethusdt"]
WS_URL = f"wss://stream.binance.com:9443/stream?streams={'/'.join([s + '@trade' for s in SYMBOLS])}"

async def consume():
    print("🔌 Connecting to Binance WebSocket...")
    async with websockets.connect(WS_URL) as websocket:
        print("✅ Connected. Listening for BTC and ETH price updates...\n")
        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)

                payload = data.get("data", {})
                symbol = payload.get("s")
                price = float(payload.get("p"))
                ts_ms = payload.get("T")

                # Convert to timezone-aware datetime (UTC)
                timestamp = datetime.fromtimestamp(ts_ms / 1000.0, tz=timezone.utc)

                print(f"{timestamp} | {symbol} | {price}")
                insert_price(timestamp, symbol, price)

            except Exception as e:
                print(f"⚠️ Error: {e}")
                await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(consume())
