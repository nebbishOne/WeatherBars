### my weather getter
import codecs;
from datetime import datetime as date;
import datetime;
import json; 
import os;
import time; 

### get the weather data with CURL and put it in a text file
os.chdir('C:\\Users\\Peter\\Documents\\Rainmeter\\Skins\\peter1\\weatherbars')
os.system('c:\\bat\\curl.exe -o C:\\Users\\Peter\\Documents\\Rainmeter\\Skins\\peter1\\weatherbars\\weather.json https://api.forecast.io/forecast/774bc7fa6ef96998a1825a990182b1fc/39.5348073,-104.9925671')

### read the file and pull out key bits of data
with open('C:\\Users\\Peter\\Documents\\Rainmeter\\Skins\\peter1\\weatherbars\\weather.json') as data_file:
    data = json.load(data_file)
    
data_file.close

### time 
###now
#epoch = data["currently"]["time"]
#rightnow = time.strftime("%d %b %Y %H:%M", time.localtime(epoch))
#outs = 'rightnow is ' + rightnow
#print outs

### daily 
### summary
summ = data["daily"]["summary"]
#summ = summ.encode('utf-8')
##print summ

### 7 day forecasts
dailyData = data["daily"]["data"]
spaces = "\t"

### save the data to a new file
##wFile = open('C:\\Users\\Peter\\Documents\\Rainmeter\\Skins\\peter1\\weatherbars\\weather.txt', 'w')
with codecs.open('C:\\Users\\Peter\\Documents\\Rainmeter\\Skins\\peter1\\weatherbars\\weather.txt', 'w', 'utf-8') as wFile:
    wFile.write(summ + "\n\n")
    name = todayis = date.today().strftime("%A")[0:3]
    for x in range(1,8):
        wFile.write(name + spaces)
        name = date.today() + datetime.timedelta(days=x)
        name = name.strftime("%A")[0:3]

    wFile.write("\n\n")

    maxT = 0
    minT = 0
    allMax = ""
    allMin = ""

    ### get the 7 days' data
    spaces = "\t"
    for day in range(0, 7):
        t = dailyData[day]["time"]
        t = time.strftime("%b %d", time.localtime(t))
        #icon = dailyData[day]["icon"]
        tempMin = str(round(dailyData[day]["temperatureMin"],0))[:-2]
        tempMax = str(round(dailyData[day]["temperatureMax"],0))[:-2]
        
        if tempMin < minT:
            minT = tempMin
        
        if tempMax > maxT:
            maxT = tempMax
        
        allMin = allMin + tempMin + spaces 
        allMax = allMax + tempMax + spaces

    wFile.write(allMax + "\n\n\n\n\n\n")
    wFile.write(allMin + "\n\n")    

    wFile.close

print '\n done.'
