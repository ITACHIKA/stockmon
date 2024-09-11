import requests
import json
import bs4
import pandas as pd

import callGetAllCode
import callGetAllStockInfo

header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
exchange=["nasdaq","nyse","amex"]

allStockCodes=callGetAllCode.callGetAllCode(exchange,header)
fullStockInfo=callGetAllStockInfo.callGetStock(header,64,allStockCodes)