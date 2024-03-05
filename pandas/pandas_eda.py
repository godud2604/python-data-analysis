# %%
import pandas as pd

# %%
doc = pd.read_csv("COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/04-01-2020.csv", encoding='utf-8-sig')

# %% 
"""
탐색적 데이터 분석: 1. 데이터의 출처와 주제에 대해 이해
- 국가별 코로나 바이러스 daily 현황 자료
"""

# %%
"""
탐색적 데이터 분석: 2. 데이터의 크기 확인
"""
doc.head()

# %% 보다 다양한 데이터 정보 확인하기
doc.shape

# %%
doc.info()

# %%
"""
탐색적 데이터 분석: 3. 데이터 구성 요소(feature)의 속성(특징) 확인
- Country_Region: 국가, Lat/Long: 경도, Confirmed: 확진, Deaths: 사망, Recovered: 회복, Active: 확진 중인 사람(사망자/회복자 제외)
"""

# %% 각 column 이해하기
doc.columns

# %% 속성이 숫자라면, 평균, 표준편차, 4분위 수, 최소/최대값 확인
doc.describe()

# %% 속성간 상관관계 이해하기
doc.corr(numeric_only=True)

# %%
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,10))
sns.heatmap(data = doc.corr(numeric_only=True), annot=True, fmt = '.2f', linewidths=0.5, cmap='Blues')
# %%
