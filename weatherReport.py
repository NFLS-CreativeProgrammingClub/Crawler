#爬取某市十年天气预报
#城市名在22行，26行修改
#代码：TwiShi

import re
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
dates, conditions, temperatures, winds = [], [], [], []

def get_data(url):
    html = rq.get(url).content.decode("gbk")
    soup = BeautifulSoup(html, "html.parser")
    tr_list = soup.find_all("tr")
    for data in tr_list[1:]:
        sub_data = data.text.split()
        dates.append(sub_data[0])
        conditions.append("".join(sub_data[1:3]))
        temperatures.append("".join(sub_data[3:6]))
        winds.append("".join(sub_data[6:10]))

file1=open("Shanghai_History_Weather.txt","w")
x=["01","02","03","04","05","06","07","08","09","10","11","12"]
for i in range(2011,2021):
    for j in x:
        get_data("http://www.tianqihoubao.com/lishi/shanghai/month/"+str(i)+j+".html")
        for k in range(0,len(dates)):
            file1.write(dates[k]+" "+conditions[k]+" "+temperatures[k]+" "+winds[k]+"\n")
#            print(dates[k],conditions[k],temperatures[k],winds[k])
        print(str(i)+j+"ok")
print("AC")
file1.close()
# data.to_csv("guangzhou_history_weather_data.csv", index=False, encoding="utf-8")