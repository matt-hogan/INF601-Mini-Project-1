# INF601 - Advanced Programming in Python
# Matt Hogan
# Mini Project 1

# Imports
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import os

ticker_names = [ "TSLA", "AAPL", "META", "AMZN", "MSFT" ]
# Get stock data for the last 10 days
data = yf.download(
    tickers=ticker_names,
    start="2022-09-02",
    end="2022-09-17",
)

def get_closing_prices(ticker):
    """ Returns a list of the Adj Close prices for the provided ticker """
    return [ price for price in data["Adj Close"][ticker] ]

for ticker in ticker_names:
    ticker_prices = np.array(get_closing_prices(ticker))
    plt.plot(ticker_prices)
    plt.title(f"{ticker} Closing Stock Price For the Last 10 Days")
    plt.xlabel("Day")
    plt.ylabel("Price ($)")
    plt.close()
