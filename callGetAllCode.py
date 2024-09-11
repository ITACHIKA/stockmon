import requests
import json

def callGetAllCode(exchanges,header):
    stockCodes=[]
    for exg in exchanges:
        allStockAddr="https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=100000&exchange="+exg+"&marketcap=nano"
        allStockData=requests.get(allStockAddr,headers=header,timeout=10).text
        #print(allStockData)
        allStockJson=json.loads(allStockData)
        #print(allStockJson)
        allStockJson=allStockJson["data"]["table"]["rows"]
        for firm in allStockJson:
            stockCodes.append(firm["symbol"])
    return stockCodes