import json
import datetime

stock=""
with open("test.json","+r") as f:
    stock+=f.readline()
print(stock)
stockJson=json.loads(stock)
symbol=stockJson["chart"]["result"][0]["meta"]["symbol"]
try:
    timestamp=stockJson["chart"]["result"][0]["timestamp"][0]
    openPrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["open"][0]
    closePrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["close"][0]
    lowPrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["low"][0]
    highPrice=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["high"][0]
    volume=stockJson["chart"]["result"][0]["indicators"]["quote"][0]["volume"][0]
    print([symbol,timestamp,openPrice,closePrice,lowPrice,highPrice,volume])
except Exception as e:
    #print("error")
    #print(e)
    timestamp=0
    openPrice=-1
    closePrice=-1
    lowPrice=-1
    highPrice=-1
    volume=0
    print([symbol,timestamp,openPrice,closePrice,lowPrice,highPrice,volume])