"""

@author: 융
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests

#새로운 어제 공지 데이터 엑셀에 저장

def yesterday_crawling_s():
    #페이지 url p_url=p_+i+url
    p_="https://grandpark.seoul.go.kr/korea_grand/board/list.do?currentPage="
    url="&parentId=41216&bbsId=26&lineCnt=10&encodeYn=N&menuid=41213&headerId=41181&currentPage=1&search_target_v=%BC%AD%BF%EF%B4%EB%B0%F8%BF%F8&searchOption=combi"
    #href url: final=ur+a_num+rl
    ur="https://grandpark.seoul.go.kr/korea_grand/board/view.do?boardSeq="
    a_num=[]#'39616'#href에서 숫자만 받아온 값
    rl="&headerId=41181&menuid=41213&parentId=41216&bbsId=26"
    #final=ur+a_num[i]+rl
    #첫 게시물 링크:39616
    #
    title=[]
    href=[]
    for i in range(0,2):
        p_url=p_+str(i)+url
        html=requests.get(p_url)
        soup=BeautifulSoup(html.content.decode('euc-kr','replace'))
        t=soup.find_all('td',class_='subject')
        #print("티",t)
        
        for link in t:
           # print(link.find_all('a'))
            a_list=link.find_all('a')
            for notice in a_list:
                title.append(notice.text) 
                a_num.append(notice.get('href')[19:24])
                href.append(ur+a_num[-1]+rl)
   # print("최ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ종 리스트",href,"\n", title)
    #만약 리스트에 같은 글이 두번 있다면 더 뒤에 있는 순서의 타이틀에 <공지>를 붙여줘야한다
    
    day=[]
    for i in range(0,2):
        p_url=p_+str(i)+url
        html=requests.get(p_url)
        soup=BeautifulSoup(html.content.decode('euc-kr','replace'))
        c=soup.find_all('td',class_='date')
        for link in c:
            d=link.text
            #print(d)
            day.append(d)
    dict0=[0]*len(day)
    dict1=[0]*len(day)
    dict2=[0]*len(day)
    for i in range(len(day)):
        j=len(day)-i-1
        dict0[j]=title[i]
        dict1[j]=href[i]
        dict2[j]=day[i]
        
    for i in range(len(dict0)):
        j=len(dict0)-i-1
        if dict0[j] in dict0[:j]:
            dict0[j]='<공지>'+dict0[j]
        else:
            break
        
    data={"title":dict0,"href":dict1,"day":dict2}
   # print("최종데이터!!!!!!!!!!!!!!!!!!!!!\n",data)
    db=pd.DataFrame(data,columns=["title","href","day"])
    db.to_csv('/home/ec2-user/venv/project/FourBoxes/notice_seoul.csv', encoding='cp949')
yesterday_crawling_s()
   
#70개 데이터 엑셀에 저장

###그전날에 해당하는 게시물 가져오기 기존 엑셀에서 마지막 칸 번호 알아내서 그 밑에 
