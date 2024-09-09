import requests
import json
import bs4
import pandas as pd

header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

cap=["nano,micro,small,medium,large,mega"]
exchange=["nasdaq,nyse,amex"]

allStockAddr="https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=1600&exchange=NASDAQ&marketcap=nano"
yahoofinanceAPI="https://query2.finance.yahoo.com/v8/finance/chart/KXIN?period1=1725568800&period2=1725832800&interval=1m&includePrePost=true&lang=en-US&region=US"

allStockData=requests.get(allStockAddr,headers=header,timeout=10).text

print(allStockData)

allStockJson=json.loads(allStockData)
print(allStockJson)
allStockJson=allStockJson["data"]["table"]["rows"]
stockCodes=[]
for firm in allStockJson:
    stockCodes.append(firm["symbol"])
print(stockCodes)


