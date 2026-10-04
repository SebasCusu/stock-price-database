Stock Price Tracker

A simple Python project that fetches the latest stock price using yfinance and stores the data in a local SQLite database.

Features

Fetches the latest stock price for a ticker.

Rounds the price to two decimal places.

Stores ticker and price data in SQLite.

Displays all stored records.

Uses SQL placeholders to safely insert data.

Requirements

Python 3

yfinance

Install the dependency with:

pip install yfinance


SQLite is included with Python, so no additional installation is required.

Usage

Run the program:

python main.py


Enter a stock ticker when prompted:

Enter a ticker: AAPL


The program will fetch the latest price, save it to data.db, and display all stored records.

Database

The project automatically creates a local SQLite database named data.db.

The data table contains:

id - Unique record ID

price - Stock price

ticker - Stock ticker symbol

Example Output
[(1, 252.31, 'AAPL')]

Project Structure
.
├── main.py
├── data.db
└── README.md


data.db is created automatically when the program runs.

Notes

The stock price is retrieved using yfinance and represents the latest available price provided by Yahoo Finance.
