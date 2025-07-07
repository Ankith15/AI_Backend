
# Binance WebSocket Price Precision Capture

## Overview

This project captures real-time cryptocurrency price data for **BTC/USDT** and **ETH/USDT** using Binance's WebSocket API. The data is stored in a **MySQL database** with millisecond precision, allowing accurate querying for price analytics and time-specific lookups.


---

## Features

* **Live Price Feed:** Captures real-time BTC/ETH price updates from Binance.
* **Millisecond Precision:** Timestamps stored using timezone-aware UTC format.
* **Persistent Storage:** Stores data in MySQL with `timestamp`, `symbol`, and `price`.
* **Query Capabilities:**

  * ✅ Latest price
  * ✅ Price at a specific second
  * ✅ Minimum/Maximum price in a time range

---

## Tech Stack

* **Python 3.8+**
* **Binance WebSocket API** – for real-time streaming
* **MySQL** – for persistent price storage
* **mysql-connector-python** – Python interface for MySQL
* **websockets** – handles async WebSocket streaming
* **dotenv** – loads DB config from `.env`

---

## Installation

### Prerequisites

* Python 3.8 or higher
* MySQL server (running and accessible)
* Create a MySQL database:

  ```sql
  CREATE DATABASE binance_prices;
  ```

### Clone the Repository & Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Setup

Run the schema to create the required table:

```bash
mysql -u root -p binance_prices < schema.sql
```

### Configure Environment Variables

Create a `.env` file in the root directory:

```
MYSQL_DB=binance_prices
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
```

---

## Usage

### 1. Start the WebSocket Listener

This script continuously receives price updates and stores them in MySQL:

```bash
python ws_client.py
```

### 2. Run Query Examples

To test different price-based queries:

```bash
python query_examples.py
```

You’ll see:

* ✅ Latest BTC/ETH price
* ✅ Price at a specific UTC second
* ✅ Highest and lowest prices in a time interval

---

## Project Structure

```
task5_binance_price_capture/
├── ws_client.py           # WebSocket client for live data
├── db.py                  # DB insert and query functions
├── schema.sql             # SQL script to create table
├── query_examples.py      # Demo for required queries
├── requirements.txt       # Python dependencies
├── .env                   # DB configuration
└── README.md              # Project documentation
```

---
## Video


https://github.com/user-attachments/assets/f3bd6d3d-0688-4119-8a03-6d61a635d9f2


---
## Contributing

You are welcome to fork this repository and enhance features like:

* Adding FastAPI endpoints
* Exporting CSV reports
* Visualizing data with Grafana or Matplotlib

---

## Notes

* Ensure your system clock is set to **UTC**.
* The WebSocket script is meant to run continuously.
* To simulate volume, run for at least **2–5 minutes** before querying.

