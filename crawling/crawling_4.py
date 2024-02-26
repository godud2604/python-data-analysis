# %%
import requests
from bs4 import BeautifulSoup

url = 'https://davelee-fun.github.io/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select("li.nav-item")

for item in items:
    print(item.get_text())

# %% Teddy의 선물 블로그 타이틀 가져와 출력하기
# sitetitle
items = soup.select_one(".sitetitle")
print(items.get_text())
# %% "선물하기 좋은 선물을 고르고 골라서 소개하는 블로그입니다" 서브타이틀 출력
items = soup.select_one(".mainheading .lead")
print(items.get_text().strip())
# %%
# card-text
items = soup.select(".featured-posts .card-text")

for item in items:
    print(item.get_text())
# %%
