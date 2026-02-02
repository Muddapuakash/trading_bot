BINANCE FUTURES TESTNET TRADING BOT (PYTHON)
OVERVIEW

This project is a simplified Python trading bot built for Binance Futures Testnet (USDT-M).
It allows users to place MARKET and LIMIT orders using a Command Line Interface (CLI).

The application demonstrates:

Clean project structure

Input validation

Logging

Error handling

Real-world Python backend practices

This project is intended for evaluation and learning purposes only.

FEATURES

Place MARKET orders

Place LIMIT orders

BUY and SELL supported

Binance Futures Testnet (USDT-M)

CLI-based input

Input validation

Structured logging

Error handling

Dry-run mode (bonus feature)

PROJECT STRUCTURE

trading_bot/
│
├── bot/
│ ├── init.py
│ ├── client.py (Binance Futures Testnet client)
│ ├── orders.py (Market & Limit order logic)
│ ├── validators.py (Input validation)
│ ├── logging_config.py (Logging configuration)
│
├── cli.py (CLI entry point)
├── requirements.txt
├── README.md
├── .env.example
├── logs/
└── .gitignore

PREREQUISITES

Python 3.8 or higher

Binance Futures Testnet account

API Key and Secret from Binance Futures Testnet

SETUP INSTRUCTIONS
CLONE THE REPOSITORY

git clone <your-repository-url>
cd trading_bot

CREATE VIRTUAL ENVIRONMENT

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Linux / macOS:
source venv/bin/activate

INSTALL DEPENDENCIES

pip install -r requirements.txt

CONFIGURE ENVIRONMENT VARIABLES

Create a .env file using .env.example:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret

IMPORTANT:

Do NOT commit .env to GitHub

API keys must remain private

USAGE
MARKET ORDER EXAMPLE

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT ORDER EXAMPLE

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 45000

DRY-RUN MODE (NO ORDER PLACED)

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --dry-run

SAMPLE OUTPUT
================ ORDER REQUEST ================
Symbol : BTCUSDT
Side : BUY
Type : MARKET
Quantity : 0.001
=============== ORDER RESPONSE ===============
Order ID : 123456789
Status : FILLED
Executed Qty : 0.001
Avg Price : 43210.5

Order executed successfully!

LOGGING

Logs are automatically created in the logs/ directory.

Example log files:

binance_client_YYYY-MM-DD.log

market_order_YYYY-MM-DD.log

limit_order_YYYY-MM-DD.log

Logs contain:

API request details

API responses

Errors and exceptions

Timestamps and log levels

ASSUMPTIONS

This application works only with Binance Futures Testnet

No real money is used

Orders follow Binance testnet trading rules

User provides valid trading symbols

TECHNOLOGIES USED

Python 3.x

python-binance

argparse

python-dotenv

logging module

SECURITY NOTE

API credentials are stored using environment variables and are excluded from version control using .gitignore.

AUTHOR

Dharani
Junior Python Developer Candidate