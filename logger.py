import time
import datetime

def logger(msg):
    fn="log_"+str(datetime.datetime.today().year)+"-"+str(datetime.datetime.today().month)+"-"+str(datetime.datetime.today().day)+".log"
    with open("./"+fn,"a") as file:
        file.write(str(datetime.datetime.today())+" "+msg+"\n")