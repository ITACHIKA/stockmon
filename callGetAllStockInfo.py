import requests
import json
import tqdm
import threading

def callGetStock(header,threads_numb,targetStocks,start_time,end_time,interval):
    yahoofinanceAPIBaseLink="https://query2.finance.yahoo.com/v8/finance/chart/"
    threads_num=threads_numb
    threads=[]
    fullStockInfo=[]
    splitStockCode=[]
    divNumb=int(len(targetStocks)/threads_num)
    for i in range(0,threads_num):
        if(i!=(threads_num-1)):
            splitStockCode.append(targetStocks[divNumb*i:divNumb*(i+1)])
        else:
            splitStockCode.append(targetStocks[divNumb*i:len(targetStocks)])

    def requestStockDataYahoo(code):
        yahoofinanceAPIUrl=yahoofinanceAPIBaseLink+code+"?"+"period1="+start_time+"&period2="+end_time+"&interval="+interval+"&includePrePost=true&lang=en-US&region=US"
        #print(yahoofinanceAPIUrl)
        stockData=requests.get(yahoofinanceAPIUrl,headers=header,timeout=5)
        fullStockInfo.append(stockData.text)
        #print(stockData)

    def worker(codes,thread_numb):
        progress_bar = tqdm(codes,desc=f"Thread {thread_numb} Progress", position=thread_numb, leave=True,dynamic_ncols=False)
        for code in codes:
            requestStockDataYahoo(code)
            progress_bar.update(1)

    for i in range(threads_num):
        thread=threading.Thread(target=worker,args=(splitStockCode[i],i))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return fullStockInfo
