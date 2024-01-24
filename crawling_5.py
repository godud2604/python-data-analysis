# %% requests 라이브러리로 작성한 코드
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/')
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.select('h4.card-text')
for item in data:
    print(item.get_text().strip())

# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup

res = urlopen('https://davelee-fun.github.io/')
soup = BeautifulSoup(res, 'html.parser')

data = soup.select('h4.card-text')
for item in data:
    print(item.get_text().strip())

# %%
