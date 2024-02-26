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
for index in range(10):
    product_code = 215673140 + index + 1

    SQL = """INSERT INTO product VALUES('""" + str(product_code)+"""',
    '스위트바니 여름신상 5900원~롱원피스티셔츠/긴팔/반팔',23000,6900,70,'F'
    );
    """

    print(SQL)
    cursor.execute(SQL)

# %% DB에 Complete / 삽입, 갱신, 삭제 등이 모두 끝났으면 Connection 객체의 commit() 메서드를 사용하여 Commit
db.commit()

# %% DB 연결 닫기
db.close()

# %%
