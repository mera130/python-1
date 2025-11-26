import random 
import time 
def getRandomDate(startDate, endDate):
    print('printing random date between ', startDate,"and", endDate)
    randomGenerator= random.random()
    DateFormat = "%m/%d/%Y"
    startTime = time.mktime(time.strptime(startDate, DateFormat))
    endTime = time.mktime(time.strptime(endDate, DateFormat))
    
    randomTime = startTime + randomGenerator * (endTime - startTime)
    RandomDate = time.strftime(DateFormat, time.localtime(randomTime))
    return RandomDate
print('random date= ', getRandomDate('1/1/2017', '2/11/2019'))