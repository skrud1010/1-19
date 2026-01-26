import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt  # pyplot을 plt로 변경
import seaborn as sns
import datetime

# 1. 데이터 불러오기
try:
    df_pref = pd.read_csv("./trade_performance.csv", encoding="cp949")
    df_master = pd.read_csv("./country_master.csv", encoding="cp949")
except FileNotFoundError:
    print("❌ CSV 파일이 없습니다. 경로를 다시 확인해 주세요")
    exit()

# 2. 병합
df = pd.merge(df_pref, df_master, on="ctry_code", how="left")

# 3. 대륙별 성과분석
continent_states = df.groupby("continent")[["export_val", "import_val"]].sum()
continent_states["무역수지"] = continent_states["export_val"] - continent_states["import_val"]

best_continent = continent_states["무역수지"].idxmax()
print(f"분석 결과 : {best_continent} 대륙과의 거래에서 가장 큰 무역 수지 흑자가 발생했습니다")

# 4. FTA 효과 분석 (컬럼명 띄어쓰기 통일)
df["평균수출단가"] = df["export_val"] / df["weight"]
fta_ans = df.groupby("fta_status")["평균수출단가"].mean()

print("\nFTA 여부에 따른 평균 수출 단가 비교")
print(fta_ans)

# 5. 품목별 집중도 분석
# nlargest 결과에서 .index를 추출해야 정확히 필터링됩니다.
top2_hs_indices = df.groupby("hs_code")["export_val"].sum().nlargest(2).index
print(f"\n수출 상위 2개 품목 코드 : {list(top2_hs_indices)}")

top2_df = df[df["hs_code"].isin(top2_hs_indices)]
country_focus = top2_df.groupby(["hs_code", "ctry_name"])["export_val"].sum().reset_index()
print(country_focus)

# 6. 시각화 (날짜 처리 및 오타 수정)
df["ymd"] = pd.to_datetime(df["ymd"])
df["month"] = df["ymd"].dt.month

monthly = df.groupby("month")[["export_val", "import_val"]].sum()

# 한글 폰트 설정 (Windows 기준 Malgun Gothic)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(12, 6))
# monthly.index 오타 수정 및 마커 "o" 수정
plt.plot(monthly.index, monthly["export_val"], label="수출액", marker="o", linewidth=2)
plt.plot(monthly.index, monthly["import_val"], label="수입액", marker="o", linewidth=2)

plt.title("월별 수출입 실적 추이")
plt.xlabel("월(month)")
plt.ylabel("금액")
plt.legend() # 범례 표시 추가
plt.grid(True) # 그리드 추가하면 더 보기 좋습니다
plt.show()