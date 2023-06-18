import pandas as pd
import pandas_datareader as pdr
import datetime as dt

class RetrieveHistoricalData:
    #this class is responsible for getting the historical data
    def __init__(self):
        self.historicalData = pd.DataFrame()
        self.stockSymbol = ""

    def getData(self):
        #getting historical data
        """getting historical stock data
                for the back testing module"""
        start = dt.datetime(2019, 4, 19)
        end = dt.datetime(2022, 7, 22)

        self.historicalData = pdr.get_data_yahoo(self.stockSymbol, start, end)

        # reformatting dataframe to fit the required format for backtesting
        self.historicalData.drop('Adj Close', axis=1, inplace=True)
        self.historicalData = self.historicalData.reindex(columns=
                                                          ['Open', 'High', 'Low', 'Close', 'Volume'])

    def setSymbol(self, symbol):
        self.stockSymbol = symbol
