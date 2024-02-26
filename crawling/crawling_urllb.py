# %% HTTP response code
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/')

if res.status_code != 200:
    print('페이지 없음')
else:
    soup = BeautifulSoup(res.content, 'html.parser')

    data = soup.select('h4.card-text')
    for item in data:
        print(item.get_text().strip())

# %% 여러 페이지를 한 번에 크롤링하는 기법
import requests
from bs4 import BeautifulSoup

for page_num in range(10):
    if page_num == 0:
        res = requests.get('https://davelee-fun.github.io/')
    else:
        res = requests.get('https://davelee-fun.github.io/page' + str(page_num + 1))
    soup = BeautifulSoup(res.content, 'html.parser')

    data = soup.select('h4.card-text')

    for item in data:
        print(item.get_text())
# %%
