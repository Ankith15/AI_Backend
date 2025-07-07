
###  Task: Binance WebSocket Price Precision Capture

---

## 🔧 Objective Recap

Build a real-time system that:

* Consumes price updates for **BTC/USDT** and **ETH/USDT** using **Binance WebSocket**
* Stores them in a relational database with **high precision timestamps**
* Supports key queries like:

  * Latest price
  * Price at a specific second
  * Min/Max within a time range

---

## 🏗️ Architecture & Design Decisions

### 1. **Tech Stack**

* **Python**: Chosen for ease of WebSocket + DB integration
* **Binance WebSocket API**: Real-time, no auth required, JSON-stream format
* **MySQL**: Used for storing price data with millisecond precision
* **Timezone-Aware Timestamps**: Used `datetime.fromtimestamp(..., tz=timezone.utc)` for accuracy and future-proofing
* **Modular Codebase**: Separated concerns across `ws_client.py`, `db.py`, and `query_examples.py`

---

## ⚙️ Workflow

1. **WebSocket Connection**

   * Connected to Binance combined stream endpoint
   * Subscribed to `btcusdt@trade` and `ethusdt@trade` channels

2. **Price Extraction + Transformation**

   * Parsed symbol, price, and trade timestamp (in milliseconds)
   * Converted timestamps to UTC-aware datetime objects

3. **Data Storage**

   * Inserted each price tick into a MySQL table: `timestamp`, `symbol`, `price`
   * Schema supports millisecond precision using `DATETIME(3)`

4. **Query Module**

   * `query_examples.py` demonstrates:

     * Latest price
     * Price at specific second (via 1-second range logic)
     * Min/Max in a given interval

---

## 🚧 Challenges Faced

| Challenge                                            | Solution                                                                                   |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Precision mismatch** when querying exact timestamp | Replaced `=` matching with **range-based comparison** using `timestamp >= start AND < end` |
| **Datetime deprecation warning** in Python 3.12      | Migrated from `datetime.utcnow()` to `datetime.now(timezone.utc)`                          |
| **PowerShell redirection error** when creating table | Used `cmd /c` to apply MySQL schema via script                                             |
| **No query results** during early tests              | Let WebSocket run longer to collect more data points                                       |

---

## 📈 Scope for Improvement

* 🛠️ **Add REST APIs** using FastAPI for interactive querying
* 🧾 **Export data to CSV** for analytics or visualization
* 📊 **Integrate Grafana** for real-time dashboard over MySQL
* 🧪 **Unit tests** for query logic and DB inserts
* 🐳 **Dockerize setup** for easy deployment (optional as per prompt)

---

## ✅ Status

* Real-time price ingestion ✅
* MySQL storage with millisecond precision ✅
* Query module for all required use cases ✅
* Stable & production-ready core logic ✅
