# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 1


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def getClosing(ticker):
    # Get the closing price for the last trading days
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")

    #Empty list created and closing prices are added to it.
    closing_list = []
    for price in hist["Close"]:
        closing_list.append(round(price, 2))
    return closing_list


def generateGraph(stock):
    # It creates the chart folder
    try:
        # Create the charts folder
        Path("charts").mkdir()
    except FileExistsError:
        pass

    # Looping through the stocks and generating a plot for each
    stockClosing = np.array(getClosing(stock))
    days = list(range(1, len(stockClosing) + 1))

    # It plots the graph
    plt.plot(days, stockClosing)

    # Get the min and max for Y axis
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    # Set the X axis min and max
    # Form [xmin,xmax, ymin, ymax]
    plt.axis([10, 1, low_price - 2, high_price + 2])

    # Set the labels for the graph
    plt.xlabel("Days Ago")
    plt.ylabel("Closing Price")
    plt.title("Closing Price for " + stock)

    # Saves plot
    savefile = "charts/" + stock + ".png"
    plt.savefig(savefile)

    # Display the graph
    plt.show()

#Get stocks from the user
def getStocks():

    stocks = []

    print("Please add 5 stocks to graph: ")
    for i in range(1,6):
        while True:
            print("Enter stock ticker" + str(i))
            ticker = input("> ")
            try:
                print("Checking Ticker")
                stock = yf.Ticker(ticker)
                stock.info
                stocks.append(ticker)
                print("Valid Ticker")
                break
            except:
                print("It is not a valid stock.Please enter another: ")
    return stocks

# Start of the program
for stock in getStocks():
    getClosing(stock)
    generateGraph(stock)


