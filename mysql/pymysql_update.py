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
SQL = """
    UPDATE product SET
    TITLE = '달리샵린넨원피스 뷔스티에 썸머 가디건',
    ORI_PRICE=33000,
    DISCOUNT_PRICE=9900,
    DISCOUNT_PERCENT=70
    WHERE PRODUCT_CODE='215673141'
"""

cursor.execute(SQL)

# %% DB에 Complete / 삽입, 갱신, 삭제 등이 모두 끝났으면 Connection 객체의 commit() 메서드를 사용하여 Commit
db.commit()

# %% DB 연결 닫기
db.close()

# %%
