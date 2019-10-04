
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:08:40 2019
@author: 은비
"""

from flask import Flask, render_template
from datetime import datetime
from glob import glob

import pandas as pd, numpy as np
import openpyxl

# from . import notice_csv_seoul
# from . import mat
# 서영
import sys
sys.path.append("/home/ec2-user/venv/project/FourBoxes")
import predict

import yesterdaydata
import mat
import ydseoul

import notice_csv
import notice_csv_seoul

app=Flask(__name__)
M2011 = [[0]*31 for i in range(12)]
M2012 = [[0]*31 for i in range(12)]
M2013 = [[0]*31 for i in range(12)]
M2014 = [[0]*31 for i in range(12)]
M2015 = [[0]*31 for i in range(12)]
M2016 = [[0]*31 for i in range(12)]
M2017 = [[0]*31 for i in range(12)]
M2018 = [[0]*31 for i in range(12)]
M2019 = [[0]*31 for i in range(12)] 
M2011 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_castle_2011.csv')
M2012 = mat.castleM29('/home/ec2-user/venv/project/FourBoxes/total_castle_2012.csv')
M2013 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_castle_2013.csv')
M2014 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_castle_2014.csv')
M2015 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_castle_2015.csv')
M2016 = mat.castleM29('/home/ec2-user/venv/project/FourBoxes/total_castle_2016.csv')
M2017 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_castle_2017.csv')
M2018 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_castle_2018.csv')
M2019 = mat.castleM2019('/home/ec2-user/venv/project/FourBoxes/total_castle_2019_yesterday.csv')

S2011 = [[0]*31 for i in range(12)]
S2012 = [[0]*31 for i in range(12)]
S2013 = [[0]*31 for i in range(12)]
S2014 = [[0]*31 for i in range(12)]
S2015 = [[0]*31 for i in range(12)]
S2016 = [[0]*31 for i in range(12)]
S2017 = [[0]*31 for i in range(12)]
S2018 = [[0]*31 for i in range(12)]
S2019 = [[0]*31 for i in range(12)]

S2011 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_seoul_2011.csv')
S2012 = mat.castleM29('/home/ec2-user/venv/project/FourBoxes/total_seoul_2012.csv')
S2013 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_seoul_2013.csv')
S2014 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_seoul_2014.csv')
S2015 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_seoul_2015.csv')
S2016 = mat.castleM29('/home/ec2-user/venv/project/FourBoxes/total_seoul_2016.csv')
S2017 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_seoul_2017.csv')
S2018 = mat.castleM28('/home/ec2-user/venv/project/FourBoxes/total_seoul_2018.csv')
S2019 = mat.castleM2019('/home/ec2-user/venv/project/FourBoxes/total_seoul_2019_yesterday.csv')


app = Flask(__name__)


#yoon
notice_csv.yesterday_crawling()

df = pd.read_csv('/home/ec2-user/venv/project/FourBoxes/notice_castle.csv',encoding='cp949')#경로 조심
saved_title = df['title']
length=len(saved_title)
saved_href = df['href']
saved_day = df['day']

notice_csv_seoul.yesterday_crawling_s()

df2=pd.read_csv('/home/ec2-user/venv/project/FourBoxes/notice_seoul.csv',encoding='cp949')#경로 조심
saved_title_s = df2['title']
length_s=len(saved_title_s)
saved_href_s = df2['href']
saved_day_s = df2['day']
########

import predict_seoul
# 서영
value = predict.pre()
seoul_val = predict_seoul.pre_seoul()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index4')
def home_seoul():
    return render_template('index4.html')


@app.route('/preview_castle')
def preview():

    return render_template('preview_castle.html', test2011 = M2011, test2012 = M2012, test2013 = M2013, test2014 = M2014, test2015 = M2015, test2016 = M2016, test2017 = M2017, test2018 = M2018, test2019 = M2019)


    
@app.route('/preview_seoul')
def preview_seoul():
    return render_template('preview_seoul.html', seoul2011 = S2011, seoul2012 = S2012, 
                           seoul2013 = S2013, seoul2014 = S2014, seoul2015 = S2015,
                           seoul2016 = S2016, seoul2017 = S2017, seoul2018 = S2018,
                           seoul2019 = S2019)


# 서영
@app.route('/predict_castle')
def castle_predict():
    return render_template('predict_castle.html',data=value)

@app.route('/predict_seoul')
def seoul_predict():
    return render_template('predict_seoul.html',data=seoul_val)


@app.route('/map_castle')
def map_castle():
    return render_template('map_castle.html')

@app.route('/map_seoul')
def map_seoul():
    return render_template('map_seoul.html')

@app.route('/info_castle_1')
def info_castle_1():
    return render_template('info_castle_1.html')

@app.route('/info_seoul_1')
def info_seoul_1():
    return render_template('info_seoul_1.html')

@app.route('/info_castle_2')
def info_castle_2():
    return render_template('info_castle_2.html')
@app.route('/info_castle_3')
def info_castle_3():
    return render_template('info_castle_3.html')

@app.route('/index')
def home2():
    return render_template('index.html')


@app.route('/notice_castle')
def notice_castle():
    return render_template('notice_castle.html',Length=length, Title=saved_title, Href=saved_href, Day=saved_day)

@app.route('/notice_seoul')
def notice_seoul():
    return render_template('notice_seoul.html', Length_s=length_s, Title_s=saved_title_s, Href_s=saved_href_s, Day_s=saved_day_s)

@app.route('/select.html')
def select():
    return render_template('select.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')


