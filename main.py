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

msftClosing = np.array(getClosing("MSFT"))
days = list(range(1, len(msftClosing)+1))

#It plots the graph
plt.plot(msftClosing)

#Get the min and max for Y axis
prices = getClosing("MSFT")
prices.sort()
low_price = prices[0]
high_price = prices[-1]

#Set the X axis min and max
#Form [xmin,xmax, ymin, ymax]
plt.axis([10,1,low_price-2,high_price+2])

#Set the labels for the graph
plt.xlabel("Days Ago")
plt.ylabel("Closing Price")
plt.title("Closing Price for MSFT")

#Display the graph
plt.show()

