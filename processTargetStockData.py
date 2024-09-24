import json
import numpy as np
import datetime
from logger import logger

def processTargetStockData(stockData,curtime):
    targetStockData=[]
    for stock in stockData:
        logger(stock)
        stockJson=json.loads(stock)
        symbol=stockJson["chart"]["result"][0]["meta"]["symbol"]
        print(stockJson["chart"]["result"][0])
        try:
            #timestamp=stockJson["chart"]["result"][0]["timestamp"][0]
            openPrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["open"][0]
            closePrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["close"][0]
            lowPrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["low"][0]
            highPrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["high"][0]
            volume=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["volume"][0]
            targetStockData.append[symbol,timestamp,openPrice,closePrice,lowPrice,highPrice,volume]
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