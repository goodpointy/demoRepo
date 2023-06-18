from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd
import pandas_datareader as pdr
from backtesting.test import SMA, GOOG
import talib
import math

#this was confirmed by the professor that it was implemented correctly
#decorator function that determines which strategy to be used for backtesting
def decoratorGetData(method):
    def wrapper(self):
        if self.strategyName == "SmaCross":
            self.strategy = SmaCross

        elif self.strategyName == "Rsi":
            self.strategy = rsiOscillator

        elif self.strategyName == "DCA":
            self.strategy = DCA
            self.historicalData = self.historicalData * (10 ** -6)

        method(self)

    return wrapper



class StartBackTesting:
    #this class is responsible for conducting backtesting
    def __init__(self):
        self.strategyName = ""
        self.historicalData = pd.DataFrame()
        self.strategy = None
        self.cashAmount = 10000

    @decoratorGetData
    def getData(self):
        #start backtesting
        self.bt = Backtest(self.historicalData, self.strategy, cash = self.cashAmount, commission=0.002,
                           exclusive_orders=True)

    def setStratName(self, name):
        self.strategyName = name

    def setHistoricalData(self, data):
        self.historicalData = data

    def setCashAmount(self, cash):
        self.cashAmount = int(cash)


"""Backtesting.py which is a module we used has already implemented
the strategy design pattern. The class called Strategy is the 
common interface that is used by the other strategy classes

An indicator that we did use the strategy pattern is that we passed
our strategy classes as a parameter in the Backtest() 

self.strategy is a variable tha contains the strategy classes that we can pass to backtest
for example self.strategy = SmaCross

self.bt = Backtest(self.historicalData, self.strategy, cash = self.cashAmount, commission=0.002,
                           exclusive_orders=True)"""

#strategy class
class SmaCross(Strategy):
    """simple moving average crossover strat"""
    n1 = 50
    n2 = 100

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()



#strategy class
class rsiOscillator(Strategy):

    upper = range(50, 85, 5)
    lower = range(10, 45, 5)
    rsiWindow = 14

    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, self.rsiWindow)

    def next(self):
        if crossover(self.rsi, self.upper):
            self.position.close()

        elif crossover(self.lower, self.rsi):
            self.buy()

"""def decoratorInputAmountToInvest(method):
    def wrapper(self):
        self.amountToInvest = int(input("input amount to invest: "))

        method(self)

    return wrapper"""

#strategy class
class DCA(Strategy):

    amountToInvest = 10
    #@decoratorInputAmountToInvest
    def init(self):

        self.dayOfTheWeek = self.I(lambda x: x, self.data.Close.s.index.dayofweek)

    def next(self):

        if self.dayOfTheWeek[-1] == 1:
            self.buy(size = math.floor(self.amountToInvest / self.data.Close[-1]))





