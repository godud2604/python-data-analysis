# %%
import requests
from bs4 import BeautifulSoup
import pymysql

# %%
db = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="",
    db="ecommerce",
    charset="utf8"
)

# %%
cursor = db.cursor()

for page_num in range(10):
    if page_num == 0:
        res = requests.get("https://davelee-fun.github.io/")
    else:
        res = requests.get("https://davelee-fun.github.io/page" + str(page_num + 1))
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.select("div.card-body")

    for item in data:
        category = item.select_one("h2.card-title").get_text().replace("관련 상품 추천", "")
        product = item.select_one("h4.card-text").get_text().replace("상품명:", "")
        print(category, product)

        SQL = """INSERT INTO teddyproducts (TITLE, CATEGORY) VALUES('"""+product+"""','"""+category+"""');"""
        print(SQL)

        cursor.execute(SQL)

# %%
db.commit()
db.close()

# %%

cursor = db.cursor()

SQL = "SELECT * FROM teddyproducts"
cursor.execute(SQL)

rows = cursor.fetchall()

for row in rows:
    print(row)

db.close()
# %%
