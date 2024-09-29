import os
import datetime
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from callGetAllStockInfo import callGetStock
from callGetTargetStock import callGetTargetStock
from logger import logger
from getUnixTime import getUnixTime
from processTargetStockData import processTargetStockData

currentDayReady=False

workDirectory=""
header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
exchange=["nasdaq","nyse","amex"]
threads=24

hourDiff=3
targetStocks=[]

def initWorkFolder():
    try:
        global workDirectory
        workDirectory="./"+str(datetime.datetime.today().year)+"-"+str(datetime.datetime.today().month)+"-"+str(datetime.datetime.today().day)
        os.mkdir(workDirectory)
    except:
        a=10

def getTargetStock(exchange,header,threads):
    global targetStocks
    result=callGetTargetStock(header,exchange,threads,hourDiff,interval='1m')
    targetStocks=result
    logger("Updates target stock")
    with open(workDirectory+"/targetStock.txt","w") as file:
        for i in targetStocks:
            file.write(i)
            file.write("\n")

    return targetStocks

def routineGetStock():
    timePeriod=getUnixTime(600,hourDiff)
    rawStockData=callGetStock(header,threads,targetStocks,timePeriod[0],timePeriod[1],interval="1m",disp_graph=False)
    processedStockData=processTargetStockData(rawStockData,timePeriod[1])
    with open(workDirectory+"/"+str(timePeriod[1])+".txt","w") as f:
        for eachStock in processedStockData:
            for item in eachStock:
                f.write(str(item)+",")
            f.write('\n')

scheduler=BackgroundScheduler()
#scheduler.add_job(allStockCodeGetter,'cron',hour=0,minute=1,args=(exchange,header))
scheduler.add_job(initWorkFolder,'cron',hour=0,minute=0)
scheduler.add_job(getTargetStock,'cron',hour=0,minute=1,args=(exchange,header,threads))
scheduler.add_job(routineGetStock,'interval',minutes=1,max_instances=3)

initWorkFolder()
print(workDirectory)
targetStocks=getTargetStock(exchange,header,threads)

scheduler.start()

try:
    while(True):
        a=10
except (KeyboardInterrupt,SystemExit):
    print("exiting")
    scheduler.shutdown()