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

def make_dir(dir):
    """ Create folder to store pngs """
    if not os.path.exists(dir):
        os.mkdir(dir)

def get_closing_prices(ticker):
    """ Returns a list of the Adj Close prices for the provided ticker """
    return [ price for price in data["Adj Close"][ticker] ]

def create_charts(tickers):
    """ Create chart for each stock and save as png """
    charts_dir = "charts"
    make_dir(charts_dir)
    for ticker in tickers:
        ticker_prices = np.array(get_closing_prices(ticker))
        plt.plot(ticker_prices)
        plt.title(f"{ticker} Closing Stock Price For the Last 10 Days")
        plt.xlabel("Day")
        plt.ylabel("Price ($)")
        plt.savefig(os.path.join(charts_dir, f"{ticker}.png"))
        plt.close()

create_charts(ticker_names)