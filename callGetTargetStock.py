import json
from callGetAllStockInfo import callGetStock
from getUnixTime import getUnixTime
from callGetAllCode import callGetAllCode

def callGetTargetStock(header,exchange,threads,hourDiff,lowerBound,upperBound,interval='1m'):
    codes=callGetAllCode(exchange,header)
    weekPeriod=getUnixTime(6*24*60,hourDiff)
    fullStockInfo=callGetStock(header,threads,codes,weekPeriod[0],weekPeriod[1],interval)

    possibleStockCodes=[]

    for i in range(len(fullStockInfo)):
        indvStockJson=json.loads(fullStockInfo[i])
        #print(type(indvStockJson))
        #print(indvStockJson)
        try:
            regularMarketPrice=indvStockJson["chart"]["result"][0]["meta"]["regularMarketPrice"]
        except Exception:
            regularMarketPrice=114514
        if(lowerBound<=regularMarketPrice<=upperBound):
            symbol=indvStockJson["chart"]["result"][0]["meta"]["symbol"]
            if(len(symbol)<=4):
                possibleStockCodes.append(symbol)
    return possibleStockCodes