import time
import datetime

def getUnixTime(minute,hourDiff):
    curtime=datetime.datetime.now()
    prevtime=curtime-datetime.timedelta(minutes=minute)
    curtime+=datetime.timedelta(minutes=-hourDiff*60)
    prevtime+=datetime.timedelta(minutes=-hourDiff*60)
    unixCurtime=time.mktime(curtime.timetuple())
    unixPrevtime=time.mktime(prevtime.timetuple())
    start_time=str(int(unixPrevtime-unixPrevtime%100))
    end_time=str(int(unixCurtime-unixCurtime%100))
    return [start_time,end_time]