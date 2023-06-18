import requests, json

class GetBasicStockData():
    #this class is responsible for getting basic stock data using yahoo api
    def __init__(self):
        self.stockData = {}
        self.stockSymbol = ""

    def __str__(self):
        #print basic stock data
        output = ""
        for key, value in self.stockData.items():
            output += f'{key}: {value}' + '\n'

        return output

    def getData(self):
        #getting basic stock data using yahoo api
        url = "https://yfapi.net/v6/finance/quote"
        querystring = {"symbols": f"{self.stockSymbol},USD"}
        headers = {'x-api-key': "pCJyFfGicf5sG8cbj16XO95hHDCtbqFNaqNuaWvn"}
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)

        except Exception:
            pass

        # converting response.txt into a dictionary
        requestedData = json.loads(response.text)["quoteResponse"]["result"][0]
        # print(requestedData)

        try:
            self.stockData["Opening Price"] = requestedData["regularMarketOpen"]
            self.stockData["Closing Price"] = requestedData["regularMarketPreviousClose"]
            self.stockData["PE_ratio"] = requestedData["trailingPE"]
            self.stockData["PS_ratio"] = requestedData["epsForward"]
            self.stockData["bid"] = requestedData["bid"]
            self.stockData["volume"] = requestedData["regularMarketVolume"]
            self.stockData["ask"] = requestedData["ask"]
            self.stockData["High"] = requestedData["regularMarketDayHigh"]
            self.stockData["Low"] = requestedData["regularMarketDayLow"]

        except KeyError as missingKey:
            print(f'[!] error: unable to obtain {missingKey}')

    def setSymbol(self, symbol):
        self.stockSymbol = symbol

















#print(stockData["quoteResponse"]["result"])

#for i in stockData["quoteResponse"]["result"]:
    #print(i)
"""headers = {
    'x-api-key': "pCJyFfGicf5sG8cbj16XO95hHDCtbqFNaqNuaWvn"
    }
url = "https://yfapi.net/v11/finance/quoteSummary"
querystring = {"symbols":"AAPL, assetProfile"}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)"""

