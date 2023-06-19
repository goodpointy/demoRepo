
#new test
from pullBasicStockData import GetBasicStockData
import StartBackTesting
import Tentative_Portfolio
import RetrieveHistoricalData

from pythonProjects.stockProgramV3.baseClass import stockProgram



#we demo'd our adapter pattern in class and you aprroved of it
#adaptees using this adapter are pullBasicStockData and getHistoricalData
class getDataAdapter:
    def __init__(self, **adaptedMethod):
        self.__dict__.update(adaptedMethod)

def interfaceGetData(obj, symbol):
    obj.setSymbol(symbol)
    getDataAdapter(data=obj.getData())

#used by
#backtesting
def interfaceBackTest(obj, strat, historicalData):
    obj.setStratName(strat)
    #obj.setStrat()
    obj.setHistoricalData(historicalData)
    #obj.setCashAmount(cash)
    obj.getData()

def interfaceCreatePortfolio(obj, fileName):
    obj.setPortfolio()
    obj.savePortfolio(fileName)


def interfaceUpdatePortfolio(obj, fileName, symbol, data, strategy = ""):
    obj.loadPortfolio(fileName)
    obj.setSymbol(symbol)
    if symbol not in obj.portfolio:
        obj.insertNewEntry()

    if type(data) is dict:
        obj.setBasicData(data)

    else:
        obj.setBackTestResults(data, strategy)

    obj.savePortfolio(fileName)

def interfaceLoadPortfolio(obj, obj2, fileName):
    obj.loadPortfolio(fileName)
    print(obj)
    obj2.converter(obj.portfolio)

def main():

    #Declaring class objects
    scrapper = GetBasicStockData()
    backtesting = StartBackTesting()
    userPortfolio = Tentative_Portfolio()
    histData = RetrieveHistoricalData()
    convert = convertToJson()



    help = "lookup <stock symbol>\n" \
           "description: gets data for selected stock\n\n" \
           "createPortfolio <file name>\n" \
           "description: creates a portfolio\n\n" \
           "backtest <stock symbol> <strategy> <amount to invest>\n"\
           "        strategies: SmaCross, Rsi 10000\n"\
           "example: backtest GOOG SmaCross\n"\
           "descrtiption: backtest a stock with strategy\n\n" \
           "update <file name> <stock symbol> <optional: -bd -bt>\n"\
           "        -bd: load basic data for stock into portfolio\n" \
           "        -bt: load backtest results for stock int portfolio\n" \
           "example: update test1 GOOG -bd\n"\
           "example: update test1 GOOG -bt\n"\
           "example: update test1 GOOG -bd -bt\n"\
           "description: add stock data to a portfolio\n\n"\
           "load <file name>\n" \
           "description: loads a portfolio and displays it's contents\n\n" \
           "exit\n" \
           "description: exits program\n\n" \
           "clear\n" \
           "description: clears screen\n"

    #user input portion
    while True:
        userInput = ""
        userInput = input("enter command> ")
        cmd = userInput.split()

        if len(cmd) > 6:
            print(f"[!] {str(userInput)} is not a recognized command")
            continue

        #lookup basic stock data
        if cmd[0] == "lookup":

            #getting basic stock data and historical data
            print("basic data: ")
            interfaceGetData(scrapper, cmd[1])
            print(scrapper)
            print()


        #gather historical data and conduct backtesting
        elif cmd[0] == "backtest":
            #conducting back testing
            interfaceGetData(histData, cmd[1])
            #interfaceBackTest(backtesting, cmd[2], histData.historicalData, cmd[3])
            interfaceBackTest(backtesting, cmd[2], histData.historicalData)
            print("back testing results: ")
            print(backtesting.bt.run())
            print()


        #creating portfolio
        elif cmd[0] == "createPortfolio":
            interfaceCreatePortfolio(userPortfolio, cmd[-1])


        #update portfolio
        elif cmd[0] == "update":

            if "-bd" in cmd and len(scrapper.stockData) > 0:
                interfaceUpdatePortfolio(userPortfolio, cmd[1], cmd[2], scrapper.stockData)

            if "-bt" in cmd:
                interfaceUpdatePortfolio(userPortfolio, cmd[1], cmd[2], backtesting.bt.run(),
                                         backtesting.strategyName)


        #loading portfolio contents
        elif cmd[0] == "load":
            interfaceLoadPortfolio(userPortfolio, convert, cmd[-1])
            print(convert.jsonFile)


        elif cmd[0] == "exit":
            exit()

        elif cmd[0] == 'help':
            print(help)

        elif cmd[0] == 'clear':
            print("\n"*1000)

        else:
            print(f"[!] {userInput} is not a recognized command")

    #print(userPortfolio.portfolio)

if __name__ == '__main__':
    main()


"""file is saved as a pickle which is a python dict, when you return a pickle, if html does not 
python code, it uderstands json though, even though json and python dict is almost the same thing
if olvin, if the html he is writing needs to view the pickle, so write an adapter to convert
the pickle into a json."""