import pandas as pd
from datetime import datetime
import csv


def castleM28(f):
    with open(f, encoding='UTF-8', newline='') as g:
        j = 0
        M = [[0]*31 for i in range(12)]
        for i in range(365):
            df = pd.read_csv(f, encoding='UTF-8')
            month = df['month']
            total = df['total']
            if i!=0:
                if month[i]!= month[i-1]:
                    j=0
                else:
                    j = j+1
            M[month[i]-1][j] = total[i]
    return M

def castleM29(f):
    with open(f, encoding='UTF-8', newline='') as g:
        j = 0
        M = [[0]*31 for i in range(12)]
        for i in range(366):
            df = pd.read_csv(f, encoding='UTF-8') 
            month = df['month']
            total = df['total']
            if i!=0:
                if month[i]!= month[i-1]:
                    j=0
                else:
                    j = j+1
            M[month[i]-1][j] = total[i]
    return M

def calday(x):
    return { 1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}[x]

def castleM2019(f):
    now = datetime.now()
    numday = calday(now.month)
    if(now.year-2016)%4 == 0:
        numday = numday + 1
    numday = numday + now.day

    with open(f, encoding='UTF-8', newline='') as g:
        j = 0
        M = [[0]*31 for i in range(12)]
        for i in range(numday-1):
            df = pd.read_csv(f, encoding='UTF-8')
            month = df['month']
            total = df['predict']
            if i!=0:
                if month[i]!= month[i-1]:
                    j=0
                else:
                    j = j+1
            M[month[i]-1][j] = total[i]
    return M
