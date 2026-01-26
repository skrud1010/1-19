import pandas as pd 
import numpy as np
import time

#미션 1: 초고속 벡터 연산을 통한 수익성 분석
#내용: 10,000개의 거래 데이터에 대해 반복문(for)을 사용하지 않고, 단 한 줄의 코드로 다음 지표들을 계산하세요.
#logistics_cost (물류비용): 수출액 $\times$ 물류비 비율
#tax_cost (관세): 수출액 $\times$ 관세율
#net_profit (최종 순수익): 수출액 $-$ 물류비용 $-$ 관세
#목표: 계산 완료 후 전체 거래의 평균 순수익을 산출하세요.

try :
    # 파일 인코딩은 데이터 환경에 따라 'utf-8' 또는 'cp949' 선택
    df = pd.read_csv("./advanced_trade_data.csv", encoding="cp949")
    print(f"데이터를 성공적으로 불러왔습니다. 총 {len(df)}행")
except FileNotFoundError:
    print("파일이 없습니다. 다시 경로 수정하세요")
    exit()

# 데이터 확인
print(df.head(10))
print(df.info())

# 판다스 컬럼을 넘파이 배열로 변환
# 1. df(...) -> df[...] 로 수정
export_value = df["export_value"].values 
weight = df['weight'].values
logistics_rate = df['logistics_cost_rate'].values
tax_rate = df['tax_rate'].values
region_code = df['region_code'].values

# 결과 확인
print(export_value) # export_val 대신 export_value 사용

start_time=time.time() #현재시간
logistics_cost=export_value*logistics_rate  #물류비용수출액*물류비용
print(logistics_cost)   #물류비용
tax_cost=export_value*tax_rate #관세=수출액+관세율
net_profit=export_value-logistics_cost-tax_cost #최종 순이익=수출액-물류비용-관세
end_time=time.time() 

print(f"연산 완료 시간 : {end_time-start_time}초")
print(f"전체 순이익 : {net_profit}")
print(f"전체 평균 순이익 : {np.mean(net_profit):.2f}")





#미션 2: 데이터 분포 파악을 위한 통계 지표 산출
#내용: 우리 회사의 수출 실적이 어떤 분포를 보이는지 확인하기 위해 다음 수치를 구하세요.
#수출액의 중앙값(Median)
#실적의 변동성을 보여주는 표준편차(Standard Deviation)
#고액 거래의 기준점이 되는 상위 5% 경계값(95th Percentile)

print("\n 주요 지표 통계 분석")
print(f"  - 수출액 중앙값 : {np.median(export_value):,.2f} ")
print(f"  - 수출액 표준편차 : {np.std(export_value):,.2f} ")
print(f"  - 수출액 상위 5% 경계값 : {np.percentile(export_value, 95):,.2f} ")




#미션3 : 불리언 마스킹을 이용한 우량 거래 필터링
#내용 : 특정 조건을 만족하는 '우량 거래' 데이터만 따로 추출하여 분석
#조건: 수출액이 $150,000$ 달러 이상이면서, 동시에 물류비 비율이 $10\%$($0.10$) 이하인 거래
#목표 : 해당 조건을 만족하는 거래 건수와 총 수출액 합계를 출력하세요

prime_mark=(export_value >=150000) & (logistics_rate<=0.10)
print(prime_mark)  #[ True False  True ... False False False]

print_trades=export_value[prime_mark]
print(prime_mark)  #[ True False  True ... False False False]

print(f"\n 우량 거래 필터링 결과")
print(f" -해당 건수 : {len(print_trades)}건")
print(f" -해당거래 총 수출액 : {np.sum(print_trades):,.2f}")




#미션 4: 행렬 곱셈(@)을 활용한 지역별 시장 매력도 평가
#내용: 아시아, 유럽, 북미, 기타 4개 지역의 평균 지표를 기반으로 종합 매력도 점수를 산출하세요.
#행렬 A: 각 지역별 [평균 수출액(만달러 단위), 평균 물류비율, 평균 관세율] 데이터를 4x3 행렬로 구성하세요.
#행렬 B: 평가 가중치 [수출액: $0.5$, 물류비: $-0.25$, 관세: $-0.25$]를 3x1 벡터로 정의하세요.
#목표: @ 연산자를 사용하여 지역별 종합 점수를 구하고, 어떤 지역의 점수가 가장 높은지 비교하세요

region_metrics = []
unique_region=np.unique(region_code)
print(unique_region)

for r in unique_region :
    mask = (region_code == r)
    region_metrics.append([
        np.mean(export_value[mask]),
        np.mean(logistics_rate[mask]),
        np.mean(tax_rate[mask])
    ])

A=np.array([
    [0.5],
    [-0.25],
    [-0.25]
])
print(region_metrics)
B=np.array(region_metrics)
print(A)
print(B)

market=B@A

print("\n 지역별 시장 매력도 점수")

region_name = ["아시아", "유럽", "북미", "기타"]

for i, name in enumerate(region_name) :
    print(f" - {name} 지역의 종합 점수 : {market[i,0]:.2f}")



#미션 5: 이상치(Outlier) 발견 및 데이터 보정
#내용: 물류비 비율 데이터 중 시스템 오류로 의심되는 이상치를 찾아 정상화하세요.
#조건: 물류비 비율이 $15\%$($0.15$)를 초과하는 데이터
#목표: np.where 함수를 사용하여 해당 데이터를 전체 평균 물류비 비율로 대체(Replace)하고, 보정 전후의 최대 물류비율 변화를 확인하세요.

avg_log=np.mean(logistics_rate)
cleaned_log=np.where(logistics_rate>0.15, avg_log, logistics_rate)
print(f"\n 데이터 보정 완료")
print(f" - 보정 전 최대 물류 비용 : {np.max(logistics_rate):.2%}")
print(f" - 보정 후 최대 물류 비용 : {np.max(cleaned_log):.2%}")