# (5/5 points) Initial comments with your name, class and project at the top of your .py file.

# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 1


# (5/5 points) Proper import of packages used.
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pprint

# Ticker for Apple is APPL
# Ticker for Microsoft is MSFT
# Ticker for Adobe is ADBE
# Ticker for Alphabet is GOOG
# Ticker for NVIDIA is NVDA

def getClosing(ticker):
    # Get the closing price for the last trading days
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")

    closing_list = []
    for price in hist["Close"]:
        closing_list.append(round(price,2))
    return closing_list

msft = getClosing("MSFT")
print(msft)

