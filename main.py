import datetime
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from callGetAllStockInfo import callGetStock
from callGetTargetStock import callGetTargetStock
from logger import logger

header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
exchange=["nasdaq","nyse","amex"]
threads=16

targetStocks=[]

def getTargetStock(exchange,header):
    result=callGetTargetStock(exchange,header,threads,interval='1m')
    targetStocks=result
    logger("Updates target stock")
    return targetStocks

allStockCodes=[]
scheduler=BackgroundScheduler()
#scheduler.add_job(allStockCodeGetter,'cron',hour=0,minute=1,args=(exchange,header))
scheduler.add_job(getTargetStock,'cron',hour=0,minute=1,args=(exchange,header,threads))