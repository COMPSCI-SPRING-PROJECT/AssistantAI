from datetime import datetime as dt
from datetime import date, timedelta
import time

def getTime():
    return dt.now().strftime("%H:%M:%S")

def getDate():
    return date.today()

class timer():
    #self.timerFinish




    #def setAlarm():



    #duration in seconds
    def startTimer(self, duration):
        d = timedelta(seconds = duration)
        self.timerFinish = dt.now() + d

    def checkTimer(self):
        return (dt.now() >= self.timerFinish)

clock = timer()
clock.startTimer(3)
time.sleep(1)
print(clock.checkTimer())