# %%
"""
Pandas 라이브러리로 데이터 처리하기

1. Series로 feature를 보다 상세하게 탐색하기
- 코로나 바이러스 데이터와 함께 Pandas 라이브러리 익히기
"""

# %%
import pandas as pd
PATH = "COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"
doc = pd.read_csv(PATH + "04-01-2020.csv", encoding='utf-8-sig')

# %%
"""
데이터프레임에서 Series 추출하기
- 하나의 feature(column)만 선택하면 됨
"""

countries = doc["Country_Region"]
countries.head()

# %%
"""
Series로 feature를 보다 상세하게 탐색하기
- size : 사이즈 반환
- count() : 데이터가 없는 경우를 뺀 사이즈 반환
- unique() : 유일한 값만 반환
- value_counts() : 데이터가 없는 경우를 제외하고, 각 값의 갯수를 반환
"""
print(countries.size, countries.count())

# %%
print(countries.unique(), len(countries.unique()))

# %%
print(countries.value_counts())

# %%
"""
2. 필요한 컬럼만 선택하기
- 여러 컬럼을 선택하면, 별도의 데이터프레임이 된다
"""

covid_stat = doc[['Confirmed', 'Deaths', 'Recovered']]
covid_stat.head()

# %%
"""
3. 특정 조건에 맞는 row 검색하기
"""
doc = pd.read_csv(PATH + "04-01-2020.csv", encoding='utf-8-sig')

# %%
doc[doc['Country_Region'] == 'US']

# %%
"""
4. 없는 데이터(NaN) 처리하기
- 없는 데이터(결측치)가 있는지 확인하기
=> isnull() : 없는 데이터가 있는지 확인 (True or False)
=> sum() : 없는 데이터가 있는 행의 갯수 확인
=> 통상 isnull().sum() 으로 사용한다.
"""

# %%
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding="utf-8-sig")
doc.isnull().sum()

# %%
"""
없는 데이터 삭제하기
"""
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding="utf-8-sig")
doc = doc.dropna()
doc.head()

# %%
"""
특정 컬럼값이 없는 데이터만 삭제하기
- subset으로 해당 컬럼을 지정해줌
"""
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding="utf-8-sig")
doc = doc.dropna(subset=["Confirmed"])
doc.head()

# %%
"""
없는 데이터(NaN)을 특정값으로 일괄 변경하기
- fillna(특정값) : 특정값으로 결측치를 대체
"""
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding="utf-8-sig")
doc = doc.fillna(0)
doc.head()

# %%
"""
없는 데이터(NaN)중 특정 컬럼에 대해 특정 값으로 일괄 변경하기
- 별도 사전 데이터를 생성, 없는 데이터를 변경할 컬럼명만 키로 만들고, 변경할 특정 값을 키값으로 넣고, fillna() 함수에 적용해주면 된다.
"""
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding="utf-8-sig")
nan_data = {"Deaths": 0, "Recovered": 0}
doc = doc.fillna(nan_data)
doc.head()

# %%
"""
6. 특정 키값을 기준으로 데이터 합치기
- groupby() : SQL 구문의 group by와 동일, 특정 컬럼을 기준으로 그룹
- sum() : 그룹으로 되어 있는 데이터를 합치기
"""

doc = pd.read_csv(PATH + "04-01-2020.csv", encoding="utf-8-sig")
doc.head()

# %%
# groupby에 의해서, index가 Country_Region의 각 국가로 변경됨
doc = doc.groupby("Country_Region").sum()
doc.head()

# %%
doc.columns
# %%
doc.index
# %%
doc[doc.index == "US"]

# %%
"""
6. 컬럼 타입 변경하기
- Pandas에서 데이터 타입은 dtype으로 불리우며, 주요 데이터 타입은 다음과 같다
=> object는 파이썬의 str 또는 혼용 데이터 타입 (문자열)
=> int64는 파이썬의 int (정수)
=> float64는 파이썬의 float (부동소숫점)
=> bool는 파이썬의 bool (True 또는 False 값을 가지는 boolean)
"""

# %%
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')
doc = doc[['Country/Region', "Confirmed"]]
doc.info()

# %%
"""
- astype({컬럼명 : 변경할타입}) : 특정 컬럼의 타입을 변경
- 변경할 데이터에 없는 데이터(NaN)이 있을 경우, 에러가 날 수 있다
- Series 데이터일 경우, Series.astype(변경할 타입) 으로 쓰면 된다.
"""

doc = doc.dropna(subset=['Confirmed']) # 결측치 제거
doc = doc.astype({'Confirmed': 'int64'})
doc.info()

# %%
"""
7. 데이터프레임 컬럼명 변경하기
- columns로 컬럼명을 변경할 수 있다
"""
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')
doc = doc[['Country/Region', "Confirmed"]] # 필요한 컬럼만 선택하기

doc.columns

# %%
doc.columns = ['Country_Resion', 'Confirmed']
doc.columns

# %%
"""
8. 데이터프레임에서 중복 행 확인/제거하기
- duplicated(): 중복 행 확인하기
"""
doc.duplicated()

# %%
# 중복된 행만 확인
doc[doc.duplicated()]

# %%
"""
drop_duplicates() : 중복 행 삭제 중복값
- 특정 컬럼을 기준으로 중복 행 제거하기
=> subset = 특정컬럼

- 중복된 경우, 처음과 마지막 행 중 어느 행을 남길 것인지 결정하기
=> 처음: keep="first' (디폴트)
=> 처음; keep='last'
"""
doc = doc.drop_duplicates(subset='Country_Resion', keep='last')
doc

# %%
