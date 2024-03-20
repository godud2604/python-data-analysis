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
"""
5. 중복 데이터 합치기
- groupby() : 그룹별로 데이터를 집계하는 함수
=> 동일한 컬럼값으로 묶어서 통계 또는 평균 등을 확인할 수 있다.
"""

df = pd.DataFrame({
    '성별': ['남', '남', '남'],
    '이름': ['David', 'Dave', 'Dave'],
    '수학': [100, 50, 80],
    '국어': [80, 70, 50]
})

df

# %%
# df.groupby('이름').mean() 메서드는 숫자 컬럼에 대해서만 계산 가능
# 기존에는 df.groupby('이름').mean() 호출시, 숫자 컬럼 외에는 자동 제외하고 계산했으나, 최근 버전에서는 자동 제외되지 않으므로,
# 다음과 같이 숫자 컬럼만을 강제로 선택한 후, df.groupby('이름').mean()을 호출하면 좋을 것 같다.
selected_columns = ['이름', '수학', '국어']
df = df[selected_columns]

df.groupby('이름').mean()

# %%
df.groupby('이름').sum()

# %%
# 국가별 총 확진자수 구하기

doc = pd.read_csv(PATH + '01-22-2020.csv', encoding='utf-8-sig')

try:
    doc = doc[['Province_State', 'Country_Region', 'Confirmed']]
except:
    doc = doc[['Province/State', 'Country/Region', 'Confirmed']]
    doc.columns = ['Province_State', 'Country_Region', 'Confirmed']

doc = doc.dropna(subset=['Confirmed'])
doc = doc.astype({'Confirmed': 'int64'})
doc.head()

# %%
"""
6. 데이터 전처리
- 지금까지의 과정을 모두 한데 모아서, 함수로 만들기
1. csv 파일 읽기
2. 'Country_Region', 'Confirmed' 두 개의 컬럼만 가져오기
3. 'Confirmed'에 데이터가 없는 행 삭제하기
4. 'Country_Region'의 국가명을 여러 파일에 일관되게 변경하기
5. 'Confirmed' 데이터 타입을 int64(정수)로 변경
6. 'Country_Region'를 기준으로 중복된 데이터를 합치기
7. 파일명을 기반으로 날짜 문자열 변환하고, 'Confirmed' 컬럼명 변경하기
"""

# %%
import json

with open('COVID-19-master/csse_covid_19_data/country_convert.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)


def country_name_convert(row):
    if row['Country_Region'] in json_data:
        return json_data[row['Country_Region']]
    return row['Country_Region']

def create_dataframe(filename):
    doc = pd.read_csv(PATH + filename, encoding='utf-8-sig') # 1. csv 파일 읽기

    try:
        doc = doc[['Country_Region', 'Confirmed']] # 2. 특정 컬럼만 선택해서 데이터프레임 만들기
    except:
        doc = doc[['Country/Region', 'Confirmed']]
        doc.columns = ['Country_Region', 'Confirmed']
    
    doc = doc.dropna(subset=['Confirmed']) # 3. 특정 컬럼에 없는 데이터 삭제하기
    doc['Country_Region'] = doc.apply(country_name_convert, axis=1) # 4. Country_Region의 국가명을 여러 파일에 일관되게 변경
    doc = doc.astype({'Confirmed': 'int64'}) # 5. 특정 컬럼의 데이터 타입 변경
    doc = doc.groupby('Country_Region').sum() # 6. 특정 컬럼으로 중복된 데이터를 합치기

    # 7. 파일명을 기반으로 날짜 문자열 변환하고, 'Confirmed' 컬럼명 변경
    data_column = filename.split(".")[0].lstrip('0').replace('-', '/')
    doc.columns = [data_column]
    return doc

# %%
doc1 = create_dataframe('01-22-2020.csv')
doc2 = create_dataframe('04-01-2020.csv')
# %%
# 데이터프레임 합치기

doc = pd.merge(doc1, doc2, how='outer', left_index=True, right_index=True)
doc.head()

# %%
# 없는 데이터는 0으로 대체
doc = doc.fillna(0)
doc

# %%
"""
참고: 특정 폴더 파일 리스트 확인하기
- split() 함수를 사용해서 특정 확장자를 가진 파일 리스트만 추출 가능
- 문자열 변수.split('.')은 ['파일명', '확장자']와 같은 리스트가 반환되므로, 문자열변수.split('.')[-1]을 통해, 이 중에서 마지막 아이템을 선택
"""

import os

PATH = 'COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/'
file_list, csv_list = os.listdir(PATH), list()

for file in file_list:
    if file.split('.')[-1] == 'csv':
        csv_list.append(file)


# %%
csv_list.sort()
csv_list

# %%
import os

def generate_dataframe_by_path(PATH):
    file_list, csv_list = os.listdir(PATH), list()
    first_doc = True

    for file in file_list:
        if file.split('.')[-1] == 'csv':
            csv_list.append(file)

    csv_list.sort()

    for file in csv_list:
        doc = create_dataframe(file)
        if first_doc:
            final_doc, first_doc = doc, False                    
        else:
            final_doc = pd.merge(final_doc, doc, how='outer', left_index=True, right_index=True)

    final_doc = final_doc.fillna(0)
    return final_doc
# %%
doc = generate_dataframe_by_path(PATH)
doc

# %% 데이터 타입 변환
doc = doc.astype('int64')
doc
# %%
"""
pandas 라이브러리로 csv 파일 쓰기
- pandas dataframe 데이터를 csv파일로 저장하기 위해, to_csv() 함수 사용
   => doc.to_csv('00_data/students_default.csv")
- encoding 옵션 사용 가능
   => doc.to_csv('00_data/students_default.csv', encoding='utf-8-sig')
"""
# %%
doc.to_csv('COVID-19-master/final_df.csv')
# %%
