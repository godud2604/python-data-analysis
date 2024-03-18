# %%
import pandas as pd

# %%
df1 = pd.DataFrame({
    "id": [1,2,3],
    "customer_id": [1,2,3],
    "customer_name": ["Robert", "Peter", "Dave"]
}, columns=["id", "customer_id", "customer_name"])

# %%
df2 = pd.DataFrame({
    "id": [1,2,4],
    "order_id": [100,200,300],
    "order_date": ["2021-01-21", "2021-02-03", "2021-10-01"]
}, columns=["id", "order_id", "order_date"])

# %%
"""
concat(): 두 데이터프레임을 연결해서 하나의 데이터프레임으로 만들 수 있다
=> 두 데이터프레임을 위/아래 또는 왼쪽/오른쪽으로 연결하기만 함
=> pd.concat([데이터프레임1, 데이터프레임2])
"""
pd.concat([df1, df2])

# %%
"""
axis: 0 이면 (디폴트) 위에서 아래로 합치고, 1이면 왼쪽과 오른쪽으로 합침
"""
doc = pd.concat([df1, df2], axis=1)
doc.head()

# %%
"""
2. 두 데이터프레임 합치기 (병합하기)
- merge(): 두 데이터프레임을 합치기
=> merge(데이터프레임1, 데이터프레임2) : 두 데이터프레임에 동일한 이름을 가진 컬럼을 기준으로 두 데이터프레임을 합침
"""
pd.merge(df1, df2)

# %%
"""
- merge(데이터프레임1, 데이터프레임2, on="기준컬럼") : 기준 컬럼을 명시할 수도 있다
"""
pd.merge(df1, df2, on="id")

# %%
"""
merge()를 통해 어떻게 두 데이터프레임을 결합시킬 것인가에 대해 보다 상세한 기능을 제공함
- 결합 방법
1. inner : 내부 조인 - SQL의 INNER JOIN과 동일
2. outer : 완전 외부 조인 - SQL의 OUTER JOIN과 동일
3. left : 왼쪽 우선 외부 조인 - SQL의 LEFT JOIN과 동일
4. right : 오른쪽 우선 외부 조인 - SQL의 RIGHT JOIN과 동일

참고: merge() 함수는 SQL의 JOIN 기능과 동일
- SQL JOIN : 두 개 이상의 테이블로부터 필요한 데이터를 연결해 하나의 포괄적인 구조로 결합시키는 연산
"""
pd.merge(df1, df2, on="id", how="inner") # default: inner, 명시적으로 써주기 위해 how 옵션을 줄 수 있다

# %%
pd.merge(df1, df2, on="id", how="right")
# %%
df1 = df1.set_index('id')
df1
# %%
df2 = df2.set_index('id')
df2
# %%
pd.merge(df1, df2, left_index=True, right_index=True)
# %%
pd.merge(df1, df2, how='outer', left_index=True, right_index=True)
# %%
