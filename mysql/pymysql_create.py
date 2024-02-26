"""
데이터 삽입 (INSERT) 패턴 코드
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
ecommerce = db.cursor()

# %%
sql = """
    CREATE TABLE product (
        PRODUCT_CODE VARCHAR(20) NOT NULL,
        TITLE VARCHAR(200) NOT NULL,
        ORI_PRICE INT,
        DISCOUNT_PRICE INT,
        DISCOUNT_PERCENT INT,
        DELIVERY VARCHAR(2),
        PRIMARY KEY(PRODUCT_CODE)
    );
"""

# %% SQL 실행
ecommerce.execute(sql)

# %% DB에 Complete / 삽입, 갱신, 삭제 등이 모두 끝났으면 Connection 객체의 commit() 메서드를 사용하여 Commit
db.commit()


# %% DB 연결 닫기
db.close()
