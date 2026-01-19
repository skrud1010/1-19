import pandas as pd
#<과제1>

# 1. 데이터 불러오기 (한글 CSV → cp949 인코딩)
df = pd.read_csv("raw_trade_data.csv", encoding="cp949")   #df , cp949

# 2. HS코드를 문자열로 변환
df["hs_code"] = df["hs_code"].astype(str)

# 3. HS코드 앞 2자리가 '85'인 데이터 필터링
df_85 = df[df["hs_code"].str.startswith("85")]

# 4. 국가명이 미국 또는 베트남인 데이터만 선택
df_country = df_85[df_85["국가명"].isin(["미국", "베트남"])]

# 5. 수출금액이 0인 데이터 제외
df_nonzero = df_country[df_country["수출금액"] != 0]

# 6. 수출금액 기준 내림차순 정렬 후 상위 10개 추출
top10 = df_nonzero.sort_values(by="수출금액", ascending=False).head(10)  #sort, ascending, false : 생략하면

# 7. 결과 CSV로 저장
top10.to_csv("semiconductor_report.csv", index=False, encoding="cp949") #false

# 8. 결과 확인
print(top10)





#<과제2>
import pandas as pd

# =========================================
# 1. 데이터 불러오기
# =========================================
# 한글 CSV 파일이므로 cp949 인코딩 사용
df = pd.read_csv("raw_trade_data.csv", encoding="cp949")


# =========================================
# 2. '중량' 컬럼 결측치 처리
# =========================================
# 방법 1 (권장): 동일 품목(hs_code)별 평균 중량으로 결측치 대체

# hs_code 기준 평균 중량 계산
weight_mean_by_hs = df.groupby("hs_code")["중량"].transform("mean")

# 중량이 NaN인 경우 해당 hs_code 평균값으로 채우기
df["중량"] = df["중량"].fillna(weight_mean_by_hs)

# (만약 평균 계산이 어려운 상황이라면 아래 한 줄로 대체 가능)
# df["중량"] = df["중량"].fillna(0)


# =========================================
# 3. '수출입구분' 영문 → 국문 통일
# =========================================
# Import → 수입, Export → 수출
df["수출입구분"] = df["수출입구분"].replace({
    "Import": "수입",
    "Export": "수출"
})


# =========================================
# 4. 수출금액 단위 변환 (원 → 백만 달러)
# =========================================
# 가정 환율: 1 USD = 1,470원
EXCHANGE_RATE = 1470

# 원 → 달러 → 백만 달러 변환
df["수출금액_M_USD"] = df["수출금액"] / EXCHANGE_RATE / 1_000_000


# =========================================
# 5. 데이터 타입 검증/
# =========================================
# 각 컬럼별 dtype 확인
print(df.dtypes)

# (필요 시 수치형 컬럼을 명시적으로 변환)
df["수출금액"] = pd.to_numeric(df["수출금액"], errors="coerce")
df["중량"] = pd.to_numeric(df["중량"], errors="coerce")
df["수출금액_M_USD"] = pd.to_numeric(df["수출금액_M_USD"], errors="coerce")

# 최종 dtype 재확인
print("\n[정제 후 데이터 타입]")
print(df.dtypes)

