import json

def callGetTargetStock(fullStockInfo):

    possibleStockCodes=[]

    for i in range(len(fullStockInfo)):
        indvStockJson=json.loads(fullStockInfo[i])
        #print(type(indvStockJson))
        regularMarketPrice=indvStockJson["chart"]["result"][0]["meta"]["regularMarketPrice"]
        if(regularMarketPrice<=1):
            symbol=indvStockJson["chart"]["result"][0]["meta"]["symbol"]
            possibleStockCodes.append(symbol)
    
    return possibleStockCodes