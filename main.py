import datetime
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler

from callGetAllCode import callGetAllCode
from callGetAllStockInfo import callGetStock
from callGetTargetStock import callGetTargetStock

allStockCodes=[]
receivedStockInfo=[]

def logger(msg):
    fn="log_"+str(datetime.datetime.today().year)+"-"+str(datetime.datetime.today().month)+"-"+str(datetime.datetime.today().day)+".log"
    with open("./"+fn,"a") as file:
        file.write(str(datetime.datetime.today())+" "+msg+"\n")

def allStockCodeGetter(exchange,header):
    result=callGetAllCode(exchange,header)
    allStockCodes=result
    logger("Updates target stock")
    return allStockCodes

def stockInfoGetter(header,threads,codes,start_time,end_time,interval="1m"):
    result=callGetStock(header,threads,codes,start_time,end_time,interval)
    receivedStockInfo=result
    return result


header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
exchange=["nasdaq","nyse","amex"]
threads=16

allStockCodes=[]
scheduler=BackgroundScheduler()
scheduler.add_job(allStockCodeGetter,'cron',hour=0,minute=1,args=(exchange,header))
scheduler.add_job(stockInfoGetter,'cron',hour=0,minute=5,args=(header,threads))


#allStockCodes=callGetAllCode.callGetAllCode(exchange,header)
fullStockInfo=callGetStock(header,64,allStockCodes,)