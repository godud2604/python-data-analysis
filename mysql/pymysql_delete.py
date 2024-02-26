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
SQL = """DELETE FROM product WHERE PRODUCT_CODE ='215673142';"""

cursor.execute(SQL)

# %% DB에 Complete / 삽입, 갱신, 삭제 등이 모두 끝났으면 Connection 객체의 commit() 메서드를 사용하여 Commit
db.commit()

# %% DB 연결 닫기
db.close()

# %%
