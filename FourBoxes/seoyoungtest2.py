# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 03:04:34 2019

@author: seoyoung
"""
#import openpyxl
import pandas as pd
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#날씨


options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("http://www.weatheri.co.kr/forecast/forecast01.php?rid=0101010000&k=1&a_name=%EC%84%9C%EC%9A%B8")        
driver.implicitly_wait(5) 

t = ['MON','TUE','WEN','THU','FRI','SAT','SUN']
day=[]

day1  = datetime.now()
day2 = day1+timedelta(days=1)
day3 = day1+timedelta(days=2)
day4 = day1+timedelta(days=3)
day5 = day1+timedelta(days=4)
day6 = day1+timedelta(days=5)
day7 = day1+timedelta(days=6)
day8 = day1+timedelta(days=7)
day9 = day1+timedelta(days=8)
day10 = day1+timedelta(days=9)

day.append(day1.day)
day.append(day2.day)
day.append(day3.day)
day.append(day4.day)
day.append(day5.day)
day.append(day6.day)
day.append(day7.day)
day.append(day8.day)
day.append(day9.day)
day.append(day10.day)


time1 = datetime(2019,8,1,12,1,1)

r=2+(day1-time1).days

df = pd.read_csv('/home/ec2-user/venv/project/FourBoxes/read_predict_data.csv',encoding='cp949')#경로 조심

saved_holiday = df.holiday.tolist()
saved_night = df.night.tolist()
saved_culture = df.night.tolist()
saved_day = df['day']

holiday = saved_holiday[r-2:r+8]
night = saved_night[r-2:r+8]
culture = saved_culture[r-2:r+8]
print(saved_day[r-2:r+8])

print(holiday)
print(night)
print(culture)


img_path={
        'http://www.weatheri.co.kr/images/icon_2013_01/01.png':1,
        'http://www.weatheri.co.kr/images/icon_2013_01/02.png':2,
        'http://www.weatheri.co.kr/images/icon_2013_01/18.png':3,
        'http://www.weatheri.co.kr/images/icon_2013_01/21.png':4,
        'http://www.weatheri.co.kr/images/icon_2013_01/03.png':6,
        'http://www.weatheri.co.kr/images/icon_2013_01/13.png':7,
        'http://www.weatheri.co.kr/images/icon_2013_01/07.png':8,
        'http://www.weatheri.co.kr/images/icon_2013_01/04.png':10,
        'http://www.weatheri.co.kr/images/icon_2013_01/16.png':5,
        'http://www.weatheri.co.kr/images/icon_2013_01/11.png':5
        }

day1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[1]/b")
rain1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[4]/td[2]/font")
cloud1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[1]/img")
temp_max1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[2]/b/font")
temp_min1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[2]/b/b/font")
cloud_=cloud1.get_attribute('src')
cl1=img_path[cloud_]
print(rain1.text,cl1,temp_max1.text,temp_min1.text)

day2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/b")
rain2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/font")
cloud2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[1]/img")
temp_max2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/b/font")
temp_min2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/b/b/font")
cloud_=cloud2.get_attribute('src')

print(day2.text,rain2.text,temp_max2.text,temp_min2.text)



driver.close()
