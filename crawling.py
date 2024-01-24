# %%
import requests # 웹페이지 가져오는 라이브러리
from bs4 import BeautifulSoup # 웹페이지 분석(크롤링) 라이브러리

# 웹페이지 가져오기
res = requests.get('http://news.v.daum.net/v/20170615203441266')

# 웹페이지 파싱
soup = BeautifulSoup(res.content, 'html.parser')

mydata = soup.find_all("span", "txt_info")

for item in mydata:
    print(item.get_text())

# %%
data = soup.find_all("div", "article_view")
print('data', data)


for item in data:
    print(item.get_text())

# divdata = soup.find('p', attrs={"dmcf-ptype", "general"})
# print('divdata', divdata)
# divdata.get_text()

# %%
"""
파싱(parsing) 이란?
- 문자열의 의미 분석
"""