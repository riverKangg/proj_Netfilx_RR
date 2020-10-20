# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# 크롤링한 결과 저장할 df 만들어놓기
df = pd.DataFrame(columns=["title", "genre", "year", "netflix"])
count = 0
num=0

# 크롤링
while True:
    url = "https://www.4flix.co.kr/board/netflix/" + str(num)
    with urllib.request.urlopen(url) as url:
        try:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")
        
            title_year = soup.find_all("h1")[2].text.strip() # 제목(연도) 
            title = title_year[:-6] #제목만
            year = title_year[-5:-1] #연도만
            genre = soup.find_all("h3")[1].text.strip()
            netflix = soup.find_all("p")[0].text.strip()
        
            df.loc[count] = [title, genre, year, netflix]
            count+=1
        except:
            pass #3039는 글 지워짐 
    num+=1