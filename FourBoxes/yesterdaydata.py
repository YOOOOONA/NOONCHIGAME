# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 13:40:44 2019

@author: 은비
"""
import pandas as pd

from sklearn.externals import joblib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import csv

#모델
job = "/home/ec2-user/venv/project/eunbi_model.pkl"

with open(job, 'rb') as file:
    model = joblib.load(job)

line_counter = 0
header = []
customer_USA = []
alldata = []
yesterday = []
train = []
future = []

options = Options()
options.headless = True
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
driver.get("http://www.weatheri.co.kr/bygone/bygone06.php")

driver.implicitly_wait(5)

temper = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[44]/td[2]/font")
rain = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[44]/td[10]/font")
cloud = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[44]/td[5]/font")


now = datetime.now()
def f(x):
    return { 1:0, 2:31, 43:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 
            11:304, 12:334}[x]

numday = f(now.month)
if (now.year-2016)%4==0:
    numday = numday +1

numday = numday + now.day

with open('/home/ec2-user/venv/project/FourBoxes/total_castle_2019.csv', 'r', encoding='UTF-8', newline='') as f:
    while 1:
        data = f.readline()
        if not data: break
        if line_counter == 0:
            header = data.strip().split(",")
        else:
            customer= data.strip().split(",")
            alldata.append(customer)
            if numday-1>line_counter:
                customer_USA.append(customer)
            if numday-1<line_counter:
                future.append(customer)
        line_counter += 1
    f.close()

if rain.text=="":
    result = [temper.text, cloud.text, 0]
    yesterday = [alldata[len(customer_USA)][0],alldata[len(customer_USA)][1],'',result[0],
                                 alldata[len(customer_USA)][4], result[1], alldata[len(customer_USA)][6],
                                 alldata[len(customer_USA)][7], 0, alldata[len(customer_USA)][9],
                                 alldata[len(customer_USA)][10], 2019, alldata[len(customer_USA)][12],
                                 alldata[len(customer_USA)][13], '']
elif rain.text=='-':
    result = [temper.text, cloud.text, 0]
    yesterday = [alldata[len(customer_USA)][0],alldata[len(customer_USA)][1],'',result[0],
                                 alldata[len(customer_USA)][4], result[1], alldata[len(customer_USA)][6],
                                 alldata[len(customer_USA)][7], 0, alldata[len(customer_USA)][9],
                                 alldata[len(customer_USA)][10], 2019, alldata[len(customer_USA)][12],
                                 alldata[len(customer_USA)][13], '']
else:
    result = [temper.text, cloud.text, rain.text]
    yesterday = [alldata[len(customer_USA)][0],alldata[len(customer_USA)][1],'',result[0],
                                 alldata[len(customer_USA)][4], result[1], alldata[len(customer_USA)][6],
                                 alldata[len(customer_USA)][7], result[2], alldata[len(customer_USA)][9],
                                 alldata[len(customer_USA)][10], 2019, alldata[len(customer_USA)][12],
                                 alldata[len(customer_USA)][13], '']

with open('/home/ec2-user/venv/project/FourBoxes/total_castle_2019_yesterday.csv', 'w', newline='', encoding='UTF-8') as g:
    writer = csv.writer(g)
    writer.writerow(header)
    for customer in customer_USA:
        writer.writerow(customer)
    writer.writerow(yesterday)
    g.close()

driver.close()

with open('/home/ec2-user/venv/project/FourBoxes/total_castle_2019_yesterday.csv','r', newline='',  encoding='UTF-8') as h:    
    a = int(1)
    b = int (0)
    day_class = {
            "월":[a,b,b,b,b,b,b],
            "화":[b,a,b,b,b,b,b],
            "수":[b,b,a,b,b,b,b],
            "목":[b,b,b,a,b,b,b],
            "금":[b,b,b,b,a,b,b],
            "토":[b,b,b,b,b,a,b],
            "일":[b,b,b,b,b,b,a]
            }
    
    month_class = {
            1:[a,b,b,b,b,b,b,b,b,b,b,b],
            2:[b,a,b,b,b,b,b,b,b,b,b,b],
            3:[b,b,a,b,b,b,b,b,b,b,b,b],
            4:[b,b,b,a,b,b,b,b,b,b,b,b],
            5:[b,b,b,b,a,b,b,b,b,b,b,b],
            6:[b,b,b,b,b,a,b,b,b,b,b,b],
            7:[b,b,b,b,b,b,a,b,b,b,b,b],
            8:[b,b,b,b,b,b,b,a,b,b,b,b],
            9:[b,b,b,b,b,b,b,b,a,b,b,b],
            10:[b,b,b,b,b,b,b,b,b,a,b,b],
            11:[b,b,b,b,b,b,b,b,b,b,a,b],
            12:[b,b,b,b,b,b,b,b,b,b,b,a]
            }

    year_class = {
            2011 : [a, b, b, b, b, b, b, b, b],
            2012 : [b, a, b, b, b, b, b, b, b],
            2013 : [b, b, a, b, b, b, b, b, b],
            2014 : [b, b, b, a, b, b, b, b, b],
            2015 : [b, b, b, b, a, b, b, b, b],
            2016 : [b, b, b, b, b, a, b, b, b],
            2017 : [b, b, b, b, b, b, a, b, b],
            2018 : [b, b, b, b, b, b, b, a, b],
            2019 : [b, b, b, b, b, b, b, b, a]
            }

    x_test = [[]]
    for i in range(7):
        df = pd.read_csv('/home/ec2-user/venv/project/FourBoxes/total_castle_2019_yesterday.csv', encoding='UTF-8')#경로 조심
        train = df['day']
        x_test[0].append((day_class[train[numday-2]])[i])

    temper_mean = 11.993767885532591
    temper_std = 10.861478112519041
    cloud_mean = 4.782798092209857
    cloud_std = 3.1228935349728744
    rain_mean = 3.3722416534181243
    rain_std = 13.774925339432713    

    temp = df['temp']
    clou = df['cloud']
    rai = df['rain']
    temper = temp[numday-2] - temper_mean
    temper /=temper_std
    cloud = clou[numday-2] - cloud_mean
    cloud /= cloud_std
    rain = float(rai[numday-2]) - rain_mean
    rain /=rain_std
    
    hoiday = df['holiday+weekend']
    month = df['month']
    x_test[0].append(temper)
    x_test[0].append(hoiday[numday-2])
    x_test[0].append(cloud) 
    for i in range(12):
        x_test[0].append((month_class[month[numday-2]])[i])
    nightopen = df['NightOpen']
    closed = df['closed']
    culture = df['culture']
    x_test[0].append(nightopen[numday-2])
    x_test[0].append(rain)
    x_test[0].append(closed[numday-2])
    x_test[0].append(culture[numday-2])
    year = df['year']
    for i in range(9):
        x_test[0].append((year_class[year[numday-2]])[i])
            
    y_predict = model.predict(x_test)
    yesterday[14] = y_predict[0]
    file.close()

    with open('/home/ec2-user/venv/project/FourBoxes/total_castle_2019.csv', 'w', newline='', encoding='UTF-8') as p:
        writer = csv.writer(p)
        writer.writerow(header)
        for customer in customer_USA:
            writer.writerow(customer)
        writer.writerow(yesterday)
        for cr in future:
            writer.writerow(cr)
        p.close()

    with open('/home/ec2-user/venv/project/FourBoxes/total_castle_2019_yesterday.csv', 'w', newline='',  encoding='UTF-8') as g:
        writer = csv.writer(g)
        writer.writerow(header)
        for customer in customer_USA:
            writer.writerow(customer)
        writer.writerow(yesterday)
        g.close()
