import json
import numpy as np
import datetime
from logger import logger

def processTargetStockData(stockData,curtime):
    targetStockData=[]
    for stock in stockData:
        logger(stock)
        #print(stock)
        stock=stock.rstrip()
        stock=stock.lstrip()
        stockJson=json.loads(stock)
        symbol=stockJson["chart"]["result"][0]["meta"]["symbol"]
        try:
            timestamp=datetime.datetime.fromtimestamp(int(stockJson["chart"]["result"][0]["timestamp"][-1])).strftime("%Y-%M-%D %H:%M:%S")
            openPrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["open"][-1]
            closePrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["close"][-1]
            lowPrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["low"][-1]
            highPrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["high"][-1]
            volume=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["volume"]
            totalVolume=np.sum(volume)
            targetStockData.append([symbol,timestamp,openPrice,closePrice,lowPrice,highPrice,totalVolume])
        except Exception as e:
            #print("error")
            #print(e)
            timestamp=datetime.datetime.fromtimestamp(int(curtime))
            openPrice=-1
            closePrice=-1
            lowPrice=-1
            highPrice=-1
            volume=0
            targetStockData.append([symbol,timestamp,openPrice,closePrice,lowPrice,highPrice,volume])
    return targetStockData