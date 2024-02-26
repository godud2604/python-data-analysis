"""
1. fetchall()
- 이 메소드는 쿼리 결과의 모든 행을 가져온다.
- 결과는 튜플의 튜플로 반환된다.
- 각 내부 튜플은 하나의 레코드를 나타낸다.

cursor.execute("SELECT * FROM MyTable")
rows = cursor.fetchall()

for row in rows:
    print(row)
"""

"""
2. fetchone()
- 이 메소드는 쿼리 결과의 다음 행을 가져온다.
- 결과는 하나의 튜플로 반환되며, 튜플의 각 요소는 각 필드를 나타낸다.
- 더 이상 가져올 행이 없으면 None을 반환한다.

cursor.execute("SELECT * FROM MyTable")
row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()
"""

"""
3. fetchmany(size)
- 이 메소드는 쿼리 결과의 다음 행들을 가져온다.
- 'size'는 가져올 행의 수를 지정한다.
- 결과는 튜플의 튜플로 반환된다.

cursor.execute("SELECT * FROM MyTable")
rows = cursor.fetchmany(5)

while rows:
    print(rows)
    rows = cursor.fetchmany(5)
"""

# %%
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

# %% Cursor Object 가져오기 : cursor = db.cursor()
cursor = db.cursor()

# %%
SQL = "SELECT * FROM product"
cursor.execute(SQL)
row = cursor.fetchone()
print(row)

row = cursor.fetchone()
print(row)

# %% DB 연결 닫기
db.close()

# %%
