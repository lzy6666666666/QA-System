import time


# 获取当前时间，并返回Fx平台预期格式
def getTime():
    localtime = time.localtime(time.time())
    if localtime.tm_hour <= 9:
        timeHour = "0"+str(localtime.tm_hour)
    else:
        timeHour = str(localtime.tm_hour)
        
    if localtime.tm_min <= 9:
        timeMinute = "0"+str(localtime.tm_min)
    else:
        timeMinute = str(localtime.tm_min)
        
    if localtime.tm_sec <= 9:
        timeSecond = "0"+str(localtime.tm_sec)
    else:
        timeSecond = str(localtime.tm_sec)
# reTime = str(localtime.tm_year)+"/"+str(localtime.tm_mon)+"/"+str(localtime.tm_mday)+" "+str(localtime.tm_hour)+":"\
    #          + str(localtime.tm_min)+":"+str(localtime.tm_sec)
    reTime = str(localtime.tm_year)+"/"+str(localtime.tm_mon)+"/"+str(localtime.tm_mday)+" "+timeHour+":"\
             + timeMinute+":"+timeSecond
    print(localtime)
    print(reTime)
    return reTime


def main():
    getTime()


if __name__ == "__main__":
    main()
