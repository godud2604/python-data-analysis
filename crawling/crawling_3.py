# %%
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('.course')

for item in items:
    print(item.get_text())

# %%
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select_one('ul#dev_course_list > li.course.paid')

print(item.get_text())

# %%
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_html_css.html')

soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('tr')

for item in items:
    columns = item.select('td')
    row_str = ''

    for column in columns:
        row_str += ', ' + column.get_text()

    print('row_str', row_str[2:])
# %%
