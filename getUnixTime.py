import time
import datetime

def getUnixTime(minutes):
    curtime=datetime.datetime.now()
    prevtime=curtime-datetime.timedelta(minutes=minutes)
    unixCurtime=time.mktime(curtime.timetuple())
    unixPrevtime=time.mktime(prevtime.timetuple())
    start_time=str(int(unixPrevtime-unixPrevtime%100))
    end_time=str(int(unixCurtime-unixCurtime%100+100))
    return [start_time,end_time]