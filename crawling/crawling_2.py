# %%
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')

titles = soup.find_all('li', 'course')

for title in titles:
    print(title.get_text())
# %%

section = soup.find('ul', id="dev_course_list")
titles = section.find_all('li', 'course')

for idx, title in enumerate(titles):
    print(idx+1, title.get_text().split("[")[0].split('-')[1].strip())

# %%