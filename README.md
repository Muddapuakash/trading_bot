# Binance Futures Testnet Trading Bot (Python)

## Overview
This project is a simplified **Python trading bot** built for **Binance Futures Testnet (USDT-M)**.  
It allows users to place **MARKET**, **LIMIT**, and **STOP-LIMIT** orders using a **Command Line Interface (CLI)** and an optional **lightweight UI**.

The project demonstrates clean architecture, input validation, logging, error handling, and extensibility — aligned with real-world backend development practices.

---

## Features
- MARKET, LIMIT, and STOP-LIMIT orders
- BUY and SELL support
- Binance Futures Testnet (USDT-M)
- CLI-based execution using `argparse`
- Interactive CLI mode (menu-based)
- Dry-run mode (simulate orders safely)
- Structured logging to files
- Robust input validation and error handling
- Optional lightweight UI (Streamlit)

---

## Project Structure
trading_bot/
│
├── bot/
│ ├── init.py
│ ├── client.py # Binance Futures Testnet client
│ ├── orders.py # Order placement logic
│ ├── validators.py # Input validation
│ ├── logging_config.py # Logging configuration
│
├── cli.py # CLI entry point
├── ui.py # Optional Streamlit UI
├── requirements.txt
├── README.md
├── .env.example
├── logs/
└── .gitignore


---

## Prerequisites
- Python 3.8 or higher
- Binance Futures Testnet account
- API Key and Secret from Binance Futures Testnet

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd trading_bot
2. Create Virtual Environment
python -m venv venv
Activate:

Windows

venv\Scripts\activate
Linux / macOS

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file using .env.example:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret
⚠️ Never commit .env to GitHub.

Usage (CLI)
MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 45000
STOP-LIMIT Order (Bonus Feature)
python cli.py \
  --symbol BTCUSDT \
  --side BUY \
  --type STOP_LIMIT \
  --quantity 0.001 \
  --price 45000 \
  --stop-price 44000
Dry-Run Mode (No Order Executed)
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --dry-run
Interactive CLI Mode
python cli.py --interactive
The interactive mode guides the user through symbol, side, order type, quantity, and prices via prompts.

Optional Lightweight UI
A simple UI is implemented using Streamlit, reusing the same backend logic.

Run UI
streamlit run ui.py
The UI supports:

MARKET, LIMIT, STOP-LIMIT orders

BUY / SELL

Real-time feedback

Logging
Logs are automatically generated in the logs/ directory.

Example log files:

logs/
├── binance_client_YYYY-MM-DD.log
├── market_order_YYYY-MM-DD.log
└── limit_order_YYYY-MM-DD.log
Logs include:

API request details

API responses

Errors and exceptions

Timestamps and log levels

Assumptions
This application works only with Binance Futures Testnet

No real funds are used

Orders follow Binance testnet rules

User provides valid trading symbols

Technologies Used
Python 3.x

python-binance

argparse

python-dotenv

logging

streamlit (optional UI)

Security Note
API credentials are stored securely using environment variables and excluded from version control using .gitignore.
