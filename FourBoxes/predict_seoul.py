# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:04:28 2019

@author: seoyoung
"""

#import openpyxl
from sklearn.externals import joblib
import numpy as np
from datetime import datetime
from datetime import timedelta
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
    
def pre_seoul():    
    job = "/home/ec2-user/venv/project/FourBoxes/model_seoul.pkl"
    
    with open(job, 'rb') as file:
            model = joblib.load(job)
#    from pyvirtualdisplay import Display
#    display = Display(visible=0, size=(800, 800))  
#    display.start()      
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.weatheri.co.kr/forecast/forecast01.php?rid=0201010202&k=1&a_name=%EA%B3%BC%EC%B2%9C")
    driver.implicitly_wait(5)     
            
    week=[]
    #            visit=[]
    tem_min=[]
    tem_max=[]
    temper=[]
    holiday=[]
    cloud=[]
    weather_img=[]
    month=[]
    
    rain=[]
    rain_even=[]
    rain_noon=[]
    #           closed=[]
    
    year=[]
    w=[]
    m=[]
    h=[]
        
    a = int(1)
    b = int (0)
    week_class = {
            "MON":[a,b,b,b,b,b,b],
            "TUE":[b,a,b,b,b,b,b],
            "WEN":[b,b,a,b,b,b,b],
            "THU":[b,b,b,a,b,b,b],
            "FRI":[b,b,b,b,a,b,b],
            "SAT":[b,b,b,b,b,a,b],
            "SUN":[b,b,b,b,b,b,a]
            }
            
           
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
    
    week.append(t[day1.weekday()])
    week.append(t[day2.weekday()])
    week.append(t[day3.weekday()])
    week.append(t[day4.weekday()])
    week.append(t[day5.weekday()])
    week.append(t[day6.weekday()])
    week.append(t[day7.weekday()])
    week.append(t[day8.weekday()])
    week.append(t[day9.weekday()])
    week.append(t[day10.weekday()])
            
    month.append(day1.month)
    month.append(day2.month)
    month.append(day3.month)
    month.append(day4.month)
    month.append(day5.month)
    month.append(day6.month)
    month.append(day7.month)
    month.append(day8.month)
    month.append(day9.month)
    month.append(day10.month)
            
    year.append(day1.year)
    year.append(day2.year)
    year.append(day3.year)
    year.append(day4.year)
    year.append(day5.year)
    year.append(day6.year)
    year.append(day7.year)
    year.append(day8.year)
    year.append(day9.year)
    year.append(day10.year)
    
    value = {'year':year,'month':month,'day':day,'week':week}
    
    year=np.array(year)
    year = (year-2010)/10
            
    time1 = datetime(2019,8,1,12,1,1)

    r=2+(day1-time1).days

    holiday_class = {
               '0':0,
                "새해":1,
                "설날":1,
                "설날당일":2,
                "삼일":1,
                "어린":1,
                "석가":1,
                "현충":1,
                "광복":1,
                "추석":1,
                "추석당일":1,
                "대체":1,
                "개천":1,
                "선거":1,
                "연휴":1,
                "성탄":1,
                "한글":1}


    df = pd.read_csv('/home/ec2-user/venv/project/FourBoxes/holiday_night.csv',encoding='cp949')#경로 조심

    saved_holiday = df.holiday.tolist()
    saved_day = df['day']

    holiday = saved_holiday[r-2:r+8]

    h=np.empty(len(week))

    for i , v in enumerate(holiday):
        h[i] = holiday_class[v]


    w=np.empty((len(week),7),dtype="int")
        
    for i , v in enumerate(week):
        w[i] = week_class[v]
#    print(holiday)    
#    print(year)
#    print(month)
#    print(week)        
    
    
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
    weather_img.append(cloud_[46:])
    
    
#    print(rain1.text,cl1,temp_max1.text,temp_min1.text)
    temper.append((float(temp_max1.text[0:len(temp_max1.text)-2])+float(temp_min1.text[0:len(temp_min1.text)-2]))/2)
    tem_max.append(float(temp_max1.text[0:len(temp_max1.text)-2]))
    tem_min.append(float(temp_min1.text[0:len(temp_min1.text)-2]))
    
    if rain1.text[0:len(rain1.text)-3] == '-':
        rain.append(0)
    else: 
        rain.append(float(rain1.text[0:len(rain1.text)-3]))
    cloud.append(float(cl1))
    
    day2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/b")
    rain2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/font")
    cloud2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[1]/img")
    temp_max2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/b/font")
    temp_min2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/b/b/font")
    cloud_=cloud2.get_attribute('src')
    cl2=img_path[cloud_]
    weather_img.append(cloud_[46:])
#    print(day2.text,rain2.text,cl2,temp_max2.text,temp_min2.text)
    
    if rain2.text[0:len(rain2.text)-3] == '-':
        rain.append(0)
    else: 
        rain.append(float(rain2.text[0:len(rain2.text)-3]))
    cloud.append(float(cl2))
    
    temper.append((float(temp_max2.text[0:len(temp_max2.text)-2])+float(temp_min2.text[0:len(temp_min2.text)-2]))/2)
    tem_max.append(float(temp_max2.text[0:len(temp_max2.text)-2]))
    tem_min.append(float(temp_min2.text[0:len(temp_min2.text)-2]))
    
    
    day3=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[3]/b")
    rain3=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[4]/td[2]/font")
    cloud3=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[1]/img")
    temp_max3=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[2]/b/font")
    temp_min3=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[2]/b/b/font")
    cloud_=cloud3.get_attribute('src')
    cl3=img_path[cloud_]
    weather_img.append(cloud_[46:])
#    print(day3.text,rain3.text,cl3,temp_max3.text,temp_min3.text)
    cloud.append(float(cl3))
    
    if rain3.text[0:len(rain3.text)-3] == '-':
        rain.append(0)
    else: 
        rain.append(float(rain3.text[0:len(rain3.text)-3]))
            
    temper.append((float(temp_max3.text[0:len(temp_max3.text)-2])+float(temp_min3.text[0:len(temp_min3.text)-2]))/2)
    tem_max.append(float(temp_max3.text[0:len(temp_max3.text)-2]))
    tem_min.append(float(temp_min3.text[0:len(temp_min3.text)-2]))
    
    day4=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[4]/b")
    rain4=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[4]/table/tbody/tr[4]/td[2]/font")
    cloud4=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[1]/img")
    temp_max4=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[2]/b/font")
    temp_min4=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[2]/b/b/font")
    cloud_=cloud4.get_attribute('src')
    cl4=img_path[cloud_]
    weather_img.append(cloud_[46:])
#    print(day4.text,rain4.text,cl4,temp_max4.text,temp_min4.text)
    cloud.append(float(cl4))
    if rain4.text[0:len(rain4.text)-3] == '-':
        rain.append(0)
    else: 
        rain.append(float(rain4.text[0:len(rain4.text)-3]))
    
    temper.append((float(temp_max4.text[0:len(temp_max4.text)-2])+float(temp_min4.text[0:len(temp_min4.text)-2]))/2)
    tem_max.append(float(temp_max4.text[0:len(temp_max4.text)-2]))
    tem_min.append(float(temp_min4.text[0:len(temp_min4.text)-2]))
    
    day5=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[5]/b")
    rain5=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[5]/table/tbody/tr[4]/td[2]/font")
    cloud5=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[1]/img")
    temp_max5=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[2]/b/font")
    temp_min5=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[2]/b/b/font")
    cloud_=cloud5.get_attribute('src')
    cl5=img_path[cloud_]
    weather_img.append(cloud_[46:])
#    print(day5.text,rain5.text,cl5,temp_max5.text,temp_min5.text)
    cloud.append(float(cl5))
    if rain5.text[0:len(rain5.text)-3] == '-':
        rain.append(0)
    else: 
        rain.append(float(rain5.text[0:len(rain5.text)-3]))
    
    temper.append((float(temp_max5.text[0:len(temp_max5.text)-2])+float(temp_min5.text[0:len(temp_min5.text)-2]))/2)
    tem_max.append(float(temp_max5.text[0:len(temp_max5.text)-2]))
    tem_min.append(float(temp_min5.text[0:len(temp_min5.text)-2]))
    
    
    day6=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[1]/td[1]/b")
    rain6=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[1]/table/tbody/tr[4]/td[2]/font")
    cloud6=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[1]/img")
    temp_max6=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[2]/b/font")
    temp_min6=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[2]/b/b/font")
    cloud_=cloud6.get_attribute('src')
    cl6=img_path[cloud_]
    weather_img.append(cloud_[46:])
#    print(day6.text,rain6.text,cl6,temp_max6.text,temp_min6.text)
    cloud.append(float(cl6))
    if rain6.text[0:len(rain6.text)-3] == '-':
        rain.append(0)
    else: 
        rain.append(float(rain6.text[0:len(rain6.text)-3]))
    
    temper.append((float(temp_max6.text[0:len(temp_max6.text)-2])+float(temp_min6.text[0:len(temp_min6.text)-2]))/2)
    tem_max.append(float(temp_max6.text[0:len(temp_max6.text)-2]))
    tem_min.append(float(temp_min6.text[0:len(temp_min6.text)-2]))
    
    
    day7=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[1]/td[2]/b")
    rain7=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/font")
    cloud7=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[1]/img")
    temp_max7=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/b/font")
    temp_min7=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/b/b/font")
    cloud_=cloud7.get_attribute('src')
    cl7=img_path[cloud_]
    weather_img.append(cloud_[46:])
#    print(day7.text,rain7.text,cl7,temp_max7.text,temp_min7.text)
    cloud.append(float(cl7))
    if rain7.text[0:len(rain7.text)-3] == '-':
        rain.append(0)
    else: 
        rain.append(float(rain7.text[0:len(rain7.text)-3]))
    
    temper.append((float(temp_max7.text[0:len(temp_max7.text)-2])+float(temp_min7.text[0:len(temp_min7.text)-2]))/2)
    tem_max.append(float(temp_max7.text[0:len(temp_max7.text)-2]))
    tem_min.append(float(temp_min7.text[0:len(temp_min7.text)-2]))
    
    day8=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[1]/td[3]/b")
    rain8=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[3]/table/tbody/tr[4]/td[2]/font")
    cloud8=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[1]/img")
    temp_max8=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[2]/b/font")
    temp_min8=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[2]/b/b/font")
    cloud_=cloud8.get_attribute('src')
    cl8=img_path[cloud_]
    weather_img.append(cloud_[46:])
#    print(day8.text,rain8.text,cl8,temp_max8.text,temp_min8.text)
    cloud.append(float(cl8))
    if rain8.text[0:len(rain8.text)-3] == '-':
        rain.append(0)
    else: 
        rain.append(float(rain8.text[0:len(rain8.text)-3]))
        
    temper.append((float(temp_max8.text[0:len(temp_max8.text)-2])+float(temp_min8.text[0:len(temp_min8.text)-2]))/2)
    tem_max.append(float(temp_max8.text[0:len(temp_max8.text)-2]))
    tem_min.append(float(temp_min8.text[0:len(temp_min8.text)-2]))
    
    
    day9=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[1]/td[4]/b")
    rain9=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[4]/table/tbody/tr[4]/td[2]/font")
    cloud9=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[1]/img")
    temp_max9=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[2]/b/font")
    temp_min9=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[2]/b/b/font")
    cloud_=cloud9.get_attribute('src')
    cl9=img_path[cloud_]
#    print(day9.text,rain9.text,cl9,temp_max9.text,temp_min9.text)
    cloud.append(float(cl9))
    weather_img.append(cloud_[46:])
    
    if rain9.text[0:len(rain9.text)-3] == '-':
        rain.append(0)
    else: 
        rain.append(float(rain9.text[0:len(rain9.text)-3]))
    
    temper.append((float(temp_max9.text[0:len(temp_max9.text)-2])+float(temp_min9.text[0:len(temp_min9.text)-2]))/2)
    tem_max.append(float(temp_max9.text[0:len(temp_max9.text)-2]))
    tem_min.append(float(temp_min9.text[0:len(temp_min9.text)-2]))
    
    day10=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[1]/td[5]/b")
    rain10=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[5]/table/tbody/tr[4]/td[2]/font")
    cloud10=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[1]/img")
    temp_max10=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[2]/b/font")
    temp_min10=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[2]/b/b/font")
    cloud_=cloud10.get_attribute('src')
    cl10=img_path[cloud_]
    weather_img.append(cloud_[46:])
#    print(day10.text,rain10.text,cl10,temp_max10.text,temp_min10.text)
    cloud.append(float(cl10))
    if rain10.text[0:len(rain10.text)-3] == '-':
        rain.append(0)
    else: 
        rain.append(float(rain10.text[0:len(rain10.text)-3]))
        
    temper.append((float(temp_max10.text[0:len(temp_max10.text)-2])+float(temp_min10.text[0:len(temp_min10.text)-2]))/2)
    tem_max.append(float(temp_max10.text[0:len(temp_max10.text)-2]))
    tem_min.append(float(temp_min10.text[0:len(temp_min10.text)-2]))
    
#    print(rain)
#    print(cloud)
#    print(temper)
#    print(weather_img)
    driver.close()
    
        
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    
    url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B3%BC%EC%B2%9C+%EB%82%A0%EC%94%A8+%EC%98%88%EB%B3%B4&oquery=%EC%84%9C%EC%9A%B8+%EC%A4%91%EA%B5%AC+%EB%82%A0%EC%94%A8+%EC%98%88%EB%B3%B4&tqi=UUL2Twp0Jywss77%2BQmRsssssttw-340576"
    driver.get(url)
    driver.implicitly_wait(5)


    day1_1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul/li[1]/span[2]/span[2]/span[2]")
    day1_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul/li[1]/span[3]/span[2]/span[2]")
    
    day2_1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul/li[2]/span[2]/span[2]/span[2]")
    day2_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul/li[2]/span[3]/span[2]/span[2]")
    
    day3_1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul/li[3]/span[2]/span[2]/span[2]")
    day3_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul/li[3]/span[3]/span[2]/span[2]")
    
    day4_1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul/li[4]/span[2]/span[2]/span[2]")
    day4_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul/li[4]/span[3]/span[2]/span[2]")
    
    day5_1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul/li[5]/span[2]/span[2]/span[2]")
    day5_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul/li[5]/span[3]/span[2]/span[2]")
    
    next_weather = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]")
    next_weather.get_attribute('style')
    
    driver.execute_script("arguments[0].setAttribute('style','display:block;')",next_weather);
    
    day6_1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]/li[1]/span[2]/span[2]/span[2]")
    day6_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]/li[1]/span[3]/span[2]/span[2]")
    
    day7_1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]/li[2]/span[2]/span[2]/span[2]")
    day7_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]/li[2]/span[3]/span[2]/span[2]")
    
    day8_1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]/li[3]/span[2]/span[2]/span[2]")
    day8_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]/li[3]/span[3]/span[2]/span[2]")
    
    day9_1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]/li[4]/span[2]/span[2]/span[2]")
    day9_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]/li[4]/span[3]/span[2]/span[2]")
    
    day10_1=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]/li[5]/span[2]/span[2]/span[2]")
    day10_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[7]/ul[2]/li[5]/span[3]/span[2]/span[2]")
    
    rain_noon.append(day1_1.text)
    rain_noon.append(day2_1.text)
    rain_noon.append(day3_1.text)
    rain_noon.append(day4_1.text)
    rain_noon.append(day5_1.text)
    rain_noon.append(day6_1.text)
    rain_noon.append(day7_1.text)
    rain_noon.append(day8_1.text)
    rain_noon.append(day9_1.text)
    rain_noon.append(day10_1.text)
    
    rain_even.append(day1_2.text)
    rain_even.append(day2_2.text)
    rain_even.append(day3_2.text)
    rain_even.append(day4_2.text)
    rain_even.append(day5_2.text)
    rain_even.append(day6_2.text)
    rain_even.append(day7_2.text)
    rain_even.append(day8_2.text)
    rain_even.append(day9_2.text)
    rain_even.append(day10_2.text)
    
    driver.close()
    
    value['rain_noon']=rain_noon
    value['rain_even']=rain_even
    value['tem_min']=tem_min
    value['tem_max']=tem_max
    value['rain']=rain
    value['cloud']=cloud
    value['weather_img']=weather_img
    
    
    
    value['holiday']=h
    
    
    temper_mean = 11.9
    temper_std = 10.8
    
    rain_mean = 3.4
    rain_std = 13.93
    
    cloud_mean = 4.77
    cloud_std = 3.12
    
    temper=np.array(temper)
    temper-=temper_mean
    temper /=temper_std
    
    cloud=np.array(cloud)
    cloud-=cloud_mean
    cloud /=cloud_std
    
    rain=np.array(rain)
    rain-=rain_mean
    rain /=rain_std
    
    
    """
    1.week
    2.temper
    3.rain
    4.holiday
    5.cloud
    6.month
    7.year
    
    """
    
    x1=np.zeros((w.shape[0],w.shape[1]+1))
    x1[:,:-1]=w
    x1[:,-1]=temper
    
    
    x2=np.zeros((x1.shape[0],x1.shape[1]+1))
    x2[:,:-1]=x1
    x2[:,-1]=rain
    
    x3=np.zeros((x2.shape[0],x2.shape[1]+1))
    x3[:,:-1]=x2
    x3[:,-1]=h
    
     
    x4=np.zeros((x3.shape[0],x3.shape[1]+1))
    x4[:,:-1]=x3
    x4[:,-1]=cloud
    
    
    x5=np.zeros((x4.shape[0],x4.shape[1]+1))
    x5[:,:-1]=x4
    x5[:,-1]=month
    
    
    x6=np.zeros((x5.shape[0],x5.shape[1]+1))
    x6[:,:-1]=x5
    x6[:,-1]=year
    
    x_test=x6
    #x_test = [[1,0,0,0,0,0,0,23.5,2,0,5,9,0.9]]
    y_predict = model.predict(x_test)
    y_predict = y_predict.tolist()
    
    y_predict = [round(item) for item in y_predict]
    value['predict']=y_predict
     
#    print(value)
    file.close()   
    return value

l=pre_seoul()
print(l)
