"""

@author: 융
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests

#새로운 어제 공지 데이터 엑셀에 저장
def yesterday_crawling():
    url="http://www.royalpalace.go.kr/content/board/list.asp?p=p&c1=&c2=&page=1"#첫번째 페이지만 크롤링
    u="http://www.royalpalace.go.kr/content/board/"
    y_title=[]
    y_day=[]
    y_href=[]
    html=requests.get(url)
    soup=BeautifulSoup(html.content.decode('euc-kr','replace'))
    a=soup.find_all('a',class_='g_link')
    for link in a:
            #print(link)
            y_title.append(link.text)
            y_href.append(u+link.get('href'))
    b=soup.find_all('td',class_='m_dateSize')
    for link in b:
        y_day.append(link.text)
    #거꾸로 append하려고 새 배열에 넣기
    y_dict0=[0]*10
    y_dict1=[0]*10
    y_dict2=[0]*10
    for i in range(10):
        j=10-i-1
        y_dict0[j]=y_title[i]
        y_dict1[j]=y_href[i]
        y_dict2[j]=y_day[i]
    #기존에 있는 타이틀 빼고 data에 넣어서 프레임만들고 추가하자
    df = pd.read_csv('/home/ec2-user/venv/project/FourBoxes/notice_castle.csv',encoding='cp949')#경로 조심
    saved_title = df['title'].values.tolist()
    #print("타이틀",saved_title[67:])
    
    li=[]#번호 담기
    nli=[]
    for i,ex in enumerate(y_dict0):
        if ex in saved_title:
            li.append(int(i))
            #print("제거될 단어",ex,i)
        if ex not in saved_title:
            nli.append(int(i))
            #print("안제거된 단어",ex,i)
    
    new_title=[]
    new_href=[]
    new_day=[]
    for i in range(len(y_dict0)):
        if i not in li:
            new_title.append(y_dict0[i])
            new_href.append(y_dict1[i])
            new_day.append(y_dict2[i])
    #print("new_title",new_title)
    ##################    
    data={"title":new_title,"href":new_href,"day":new_day}
   # print("경복궁데이터!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",data)
    db=pd.DataFrame(data,columns=["title","href","day"])#프레임만들기
    db.to_csv('/home/ec2-user/venv/project/FourBoxes/notice_castle.csv', mode='a',header=False, index=False, encoding='cp949')#기존파일에 추가하기
yesterday_crawling()
'''#70개 데이터 엑셀에 저장
url="http://www.royalpalace.go.kr/content/board/list.asp?p=p&c1=&c2=&page="
u="http://www.royalpalace.go.kr/content/board/"
title=[]
href=[]
for i in range(1,8):
    URL=url+str(i)
    html=requests.get(URL)
    soup=BeautifulSoup(html.content.decode('euc-kr','replace'))
    t=soup.find_all('a',class_='g_link')
    for link in t:
        #print(link)
        title.append(link.text) 
        href.append(u+link.get('href'))
        #print(href, title)

day=[]
for i in range(1,8):
    URL=url+str(i)
    html=requests.get(URL)
    soup=BeautifulSoup(html.content.decode('euc-kr','replace'))
    c=soup.find_all('td',class_='m_dateSize')
    for link in c:
        d=link.text
        #print(d)
        day.append(d)
dict_a_with_day=[[0]*3 for j in range(len(day))]
for i in range(len(day)):
    j=len(day)-i-1
    dict_a_with_day[j][0]=title[i]
    dict_a_with_day[j][1]=href[i]
    dict_a_with_day[j][2]=day[i]
    
    
print(dict_a_with_day[0])   
    

data = pd.DataFrame(dict_a_with_day)
data.to_csv('C:Users/pc/Desktop/졸작졸작/W.T.S-/notice_castle.csv',header=False, index=False, encoding='cp949')
'''
###그전날에 해당하는 게시물 가져오기 기존 엑셀에서 마지막 칸 번호 알아내서 그 밑에 
