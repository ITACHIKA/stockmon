import json
from callGetAllStockInfo import callGetStock
from getUnixTime import getUnixTime
from callGetAllCode import callGetAllCode

def callGetTargetStock(header,exchange,threads,hourDiff,interval='1m'):
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
        if(regularMarketPrice<=1):
            symbol=indvStockJson["chart"]["result"][0]["meta"]["symbol"]
            possibleStockCodes.append(symbol)
    #logger("Updates target stock.")
    return possibleStockCodes