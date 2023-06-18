import pickle

class Tentative_Portfolio():
    #this class is responsible for creating and managing portfolio
    def __init__(self):
        self.portfolio = {}
        self.stockSymbol = ""

    def setPortfolio(self):
        self.portfolio = {}

    def insertNewEntry(self):
        #inserting a new stock into portfolio
        self.portfolio[self.stockSymbol] = {}

    def setBasicData(self, data):
        #inserting basic stock data into portfolio corresponding to its respective stock
        self.portfolio[self.stockSymbol]['basic data'] = data

    def setBackTestResults(self, backTestResults, strat):
        #inserting backtesting results corresponding to its respective stock and strategy used
        self.portfolio[self.stockSymbol][strat] = backTestResults
        #self.portfolio[self.stockSymbol]['backtesting results'] = backTestResults

    def setSymbol(self, symbol):
        self.stockSymbol = symbol


    def savePortfolio(self, filename: str = None) -> bool:
        """

        :return:
        """
        #saving portfolio as a pickle file
        if filename:
            save_file = f"{filename}.pickle"
        else:
            save_file = "portfolio1.pickle"
        try:
            with open(save_file, 'wb') as file_dump:
                pickle.dump(self.portfolio, file_dump,
                            protocol=pickle.HIGHEST_PROTOCOL)
            return True
        except Exception as e:
            print(f"File Save Exception {e}")
            return False

    def loadPortfolio(self, filename: str = None) -> bool:
        """

        :return:
        """
        #loading our portfolio
        if filename:
            save_file = f"{filename}.pickle"
        else:
            save_file = "portfolio1.pickle"
        try:
            with open(save_file, 'rb') as file_loader:
                self.portfolio = pickle.load(file_loader)
            return True
        except pickle.UnpicklingError as error:
            print(f"file load error: {error}")
            return False
        except Exception as e:
            print(f"Unknown Upload Error: {e}")
            return False

    """def output(self):
        #output portfolio contents
        flag = False
        for key, value in self.portfolio.items():
            print(f"stock: {key}\n")
            for key2, value2 in value.items():
                if type(value2) is dict:
                    print(f'{key2}: ')
                    for key3, value3 in value2.items():
                        print(f'{key3}: {value3}')

                    print()

                else:
                    if flag is False:
                        print("backtesting results: \n")
                    print(f'results for {key2}:\n')
                    print(value2)
                    print()
            print("---------------------------------------------------------")"""

    def __str__(self):
        #output portfolio contents
        flag = False
        txt = ""
        for key, value in self.portfolio.items():
            txt += f"stock: {key}\n\n"
            for key2, value2 in value.items():
                if type(value2) is dict:
                    txt += f'{key2}: \n'
                    for key3, value3 in value2.items():
                        txt += f'{key3}: {value3}\n'

                    txt += '\n'

                else:
                    if flag is False:
                        txt += "backtesting results: \n\n"
                    txt += f'results for {key2}:\n\n'
                    txt += f'{value2}  \n'
                    txt += "\n"
            txt += "---------------------------------------------------------\n"
        return txt
