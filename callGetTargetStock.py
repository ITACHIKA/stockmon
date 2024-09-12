import json
from callGetAllStockInfo import callGetStock
from getUnixTime import getUnixTime
from callGetAllCode import callGetAllCode

def callGetTargetStock(header,exchange,threads,interval='1m'):
    codes=callGetAllCode(header,exchange)
    weekPeriod=getUnixTime(7*24*60)
    fullStockInfo=callGetStock(header,threads,codes,weekPeriod[0],weekPeriod[1],interval)

    possibleStockCodes=[]

    for i in range(len(fullStockInfo)):
        indvStockJson=json.loads(fullStockInfo[i])
        #print(type(indvStockJson))
        regularMarketPrice=indvStockJson["chart"]["result"][0]["meta"]["regularMarketPrice"]
        if(regularMarketPrice<=1):
            symbol=indvStockJson["chart"]["result"][0]["meta"]["symbol"]
            possibleStockCodes.append(symbol)
    #logger("Updates target stock.")
    return possibleStockCodes