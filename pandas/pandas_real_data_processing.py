# %%
import pandas as pd
import json

PATH = "COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"
# %%
doc = pd.read_csv(PATH + "04-01-2020.csv", encoding='utf-8-sig')
doc.head()

# %%
doc = pd.read_csv(PATH + "03-01-2020.csv", encoding='utf-8-sig')
doc.head()

# %%
doc = pd.read_csv(PATH + "01-22-2020.csv", encoding='utf-8-sig')
try:
    doc = doc[['Province_State', 'Country_Region', 'Confirmed']]  # 1. 특정 컬럼만 선택해서 데이터프레임 만들기
except:
    doc = doc[['Province/State', 'Country/Region', 'Confirmed']]  # 1. 특정 컬럼만 선택해서 데이터프레임 만들기
    doc.columns = ['Province_State', 'Country_Region', 'Confirmed']
    
doc.head()

# %%
doc = doc.dropna(subset=['Confirmed']) # 특정 컬럼에 없는 데이터 삭제
doc = doc.astype({'Confirmed': 'int64'}) # 특정 컬럼의 데이터 타입 변경
doc.head()

# %% 국가 정보 가져오기
country_info = pd.read_csv("COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", encoding='utf-8-sig')
country_info.head()

# %% 두 데이터프레임 합쳐보기
test_df = pd.merge(doc, country_info, how='left', on='Country_Region')
test_df.head()

# %%
test_df.info()

# %%
"""
잘못 매칭된 국가 정보 확인
- iso2 컬럼이 매칭되지 않은 확진자수 국가 확인
"""
test_df.isnull().sum()

# %%
nan_rows = test_df[test_df['iso2'].isnull()]
nan_rows.head()

# %% json.load() 함수로 파일로된 json 데이터를 사전처럼 다룰 수 있음
with open('COVID-19-master/csse_covid_19_data/country_convert.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)
    print (json_data.keys())

# %% 
"""
Country_Region이라는 컬럼값을 확인해서, 국가명이 다르게 기재되어 있을 경우에만, 지정한 국가명으로 변경
"""
def func(row):
    if row['Country_Region'] in json_data:
        row['Country_Region'] = json_data[row['Country_Region']]
    return row

# %%
doc = doc.apply(func, axis=1)
doc.head()

# %%
