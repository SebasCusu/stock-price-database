"""Fetch a live stock price with yfinance and store it in a local SQLite database."""

import yfinance as yf
import sqlite3

def create_database():
    """Create the SQLite table if it does not already exist."""
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, price REAL, ticker TEXT)")
    connection.commit()
    connection.close()

def get_data(ticker):
    """Return the latest price for ticker, rounded to two decimal places."""
    # fast_info is a lightweight quote snapshot; last_price is the most recent trade.
    price = yf.Ticker(ticker).fast_info["last_price"]
    clean_price = round(price, 2)
    return clean_price

def insert_data(ticker, price):
    """Insert one ticker/price row. Placeholders avoid SQL injection."""
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data (price, ticker) VALUES (?, ?)", (price, ticker))
    connection.commit()
    connection.close()

def get_all_data():
    """Return every stored row as (id, price, ticker) tuples."""
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()

    connection.close()
    return data


def main():
    create_database()
    # Normalize input so "aapl" and "AAPL" map to the same symbol.
    ticker = input("Enter a ticker: ").strip().upper()
    price = get_data(ticker)
    insert_data(ticker, price)
    data = get_all_data()
    print(data)

if __name__ == "__main__":
    main()
