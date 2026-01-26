import pandas as pd
import numpy as np  
#pandas : 엑셀 + SQL + 계산기 를 파이썬으로 만든 것
#판다에서 엑셀 파일의 한 열 전체는 '시리즈' / 
#정수 범위 → range(파이썬 기본)    // 소수, 계산 포함 → np.arange  (pandas에서)


#dictionary Series(한 열)
dict_data= {"a" : 1, "b" :2, "c" :3}
series_data=pd.Series(dict_data)
print(type(series_data)) #<class 'pandas.core.series.Series'>
print(series_data)  #a    1  n\  b    2  n\  c    3  n\ dtype: int64(이 Series 안에 들어 있는 데이터의 자료형이 정수형(int64)이다)
#-> pandas는 데이터 + 메타정보(dtype) 를 함께 보여주기 때문

#list  Series(한 열)
list_data=["2026-1-19", 3.14, "abc", 100, True]
series_data=pd.Series(list_data)
print(type(series_data))  #<class 'pandas.core.series.Series'>
print(series_data) #0    2026-1-19 \n 1    3.14 \n 2   abc \n 3    100 \n 4   True \n  dtype: object(하나라도 문자열이 있으면 전부 object)

#dictionary DataFrame(여러 행과 열 전체)
dict_data = {"c0": [1,2,3], "c1": [4,5,6], "c2": [7,8,9], "c3": ["a", "b", "c"], "c4": [True, False, True]}
df = pd.DataFrame(dict_data)
print(type(df)) #<class 'pandas.core.frame.DataFrame'>
print(df)
#   c0  c1  c2 c3     c4
#0   1   4   7  a   True
#1   2   5   8  b  False
#2   3   6   9  c   True



#pandas 데이터내용 확인
# .columns : 컬럼명 확인         ex) print(df.columns)  Index(['c0', 'c1', 'c2', 'c3', 'c4'], dtype='object')
# .head() : 데이터 상단 5개행 출력   ex) print(titanic.head())
# .tail() : 데이터 하단 5개행 출력. () 안에 숫자 넣기 가능
# .shape : (행, 열) 크기 확인  ex) (3,5)
# .info() : 데이터에 대한 전반적인 정보 제공. 행과 열의 크기, 컬럼명, 컬럼별 결 측치, 컬럼별 데이터 타입 볼 수 있음
# .type() : 데이터 타입 확인


# 파일 불러오기
# 형식    읽기         쓰기
# csv   read_csv     to_csv  ex) df = pd.read_csv(파일명.csv)
# excel read_excel   to_excel
#JSON   read_json    to_json
#html   read_html    to_html
# ./ 내가 있는 기준을 하위폴더 이동 ex) ./data/
# ../내가 있는 기준으로 상위폴더 이동 ex) ../




titanic = pd.read_csv("Titanic-Dataset.csv")
#pandas에서 특정열을 선택.

# 열 1개 선택=Series(한 줄 데이터) 객체 반환
# 데이터 프레임의 열 데이터 1개만 선택할 때 2가지 방식
# 방법 1: 대괄호 + 따옴표 df["수출금액"]
# 방법 2: 점(dot) 사용   df.수출금액
#0    100
#1    200
#2    300
#Name: 수출금액, dtype: int64

# 열 n개 선택 = DataFrame (표 형태) 객체 반환
# df[["국가", "수출금액"]]
#    국가  수출금액
#0  미국   100
#1  한국   200
#2  베트남 300

# *** 열 1개인데 DataFrame으로 뽑고 싶을 때 : df[["수출금액"]]
#   수출금액
#0   100
#1   200
#2   300

names=titanic["Name"]
print(names.head())
names=titanic.Name
print(names.head())

double_columns=titanic[["Sex", "Age"]]



#< pandas 데이터 '필터링'> : 조건에 맞는 행만 남기는 것 
# 1. boolean 인덱싱 : True 값을 가진 행만 추출    df[df["수출금액"] > 0]
# 2. .isin() : 어떤 값이 데이터프레임`시리즈에 존재하면 True, 없으면 False -> df[df["국가"].isin(["미국", "베트남"])]
# 3. .isna() : 결측 값(값이 비어있다)은 True, 값이 있으면 False ->df[df["중량"].isna()]
# 4. .notna() : 값이 있으면 True, 결측 값은 False  ->df[df["중량"].notna()] 


print(double_columns["Age"]>=35)
above35=double_columns[double_columns["Age"]>=35]  #True 값만 추출했음
print(above35.head()) #그 중 위 5행

avove_male=double_columns[double_columns["Sex"]=="male"] #성별 남자만 추출
print(avove_male.head())

print(titanic.head())
class_1=titanic[titanic["Pclass"].isin([1])]  #Pclass에 1이 존재하나? 하면 T
print(class_1.head())

print(double_columns.head())
age2040=double_columns[double_columns["Age"].isin(np.arange(20,41))] #이범위에 있나 있으면 T
print(age2040.head()) 
 
print(double_columns.head(7))
class_2=double_columns["Age"].isna()
print(class_2.head(7)) #비어있는 cell T반환

class_3=double_columns["Age"].notna()
print(class_3.head(7)) #비어있는 cell F반환

print(double_columns.head(10))
age5=double_columns[double_columns["Age"].notna()] #결측 값을 제거한 누락되지 않은 값을 확인
print(age5.head(10)) #행제거



# #결측치(빈칸) 제거
# .dropna(axis=0)== .dropna() : 결측값이 들어있는 행 전체 삭제   axis=0은 행을 뜻함 
# .dropna(axis=1) : 결측값이 들어있는 열 전체 삭제    axis=1은 열을 뜻함
print(titanic.head())
print(titanic.dropna())  #결측값 있는 행 삭제
print(titanic.dropna(axis=1).head())   #결측값 있는 열 삭제



#pandas 이름과 인텍스로 특정 행과 열 '선택'
# .loc[] : 행이름과 열 이름 사용. DataFrame객체.loc[행이름, 열이름]
# .iloc[] : 행번호 열번호 사용.  DataFrame객체.iloc[행번호,열번호]
name35=titanic.loc[titanic["Age"]>=35, ["Name", "Age"]]
print(name35.head())
name35.iloc[[1,2,3],0]="No name" #0행이름값을 다 노네임으로 바꿔라
print(name35.head())



#판다스 데이터 통계
# .mean() : 평균값
# .median() : 중앙값
#.describe() : 다양한 통계량 요약
#mean, std, min, max, 25%, 50%, 75%
#.agg() : 여러개의 열에 다양한 함수 적용



#모든 열에 여러 함수를 매핑 : group.객체.agg([함수1, 함수2, 함수3,,,]) "List 방식"
#예시 group_all = df.groupby(기준열).agg([np.sum, np.mean]) 모든 열에 sum과 mean 함수 적용

#각 열마다 다른 함수를 매핑 : group.객체.agg({"열1":함수1, "열2":함수2...}) "(Dictionary 방식)"
#예시 mapping = {'열1': 'sum', '열2': ['max', 'min']}
    #group_custom = df.groupby(기준열).agg(mapping)


#.groupby() : 그룹별 집계
#.value_counts() : 값의 개수

print("----평균나이----") 
print(titanic["Age"].mean())

print("----중앙값----")
print(titanic["Age"].median())

print("----다양한 통계량 요약----")
print(titanic.describe())

print("----나이와 요금의 평균 및 표준편차----")
print(titanic[["Age", "Fare"]].agg(["mean", "std"]))


#----------영기까지

print("----열별 사용자 집계----")
agg_dict={
    "Age" : ["min", "max", "mean"],
    "Fare" : ["median", "sum"]
}
print(titanic.agg(agg_dict))

print("----성별 기준으로 평균 나이 및 요금----")
print(titanic.groupby("Sex")[["Age", "Fare"]].mean())

print("----객실 등급(Pclass)별 인원수----")
print(titanic["Pclass"].value_counts())

print("----성별 인원수----")
print(titanic["Sex"].value_counts())

print("----새로운 열 country 생성 USA----")
titanic["Country"] ="USA"
print(titanic)

print("----기존 열 계산해서 새로운 열 추가----")
titanic["NewAge"]= titanic["Age"]+10
print(titanic)

#20세 미만 child, 아니면 adult
print("----20세 미만이면 child, 아니면 adult----")
titanic["Age_group"]="Adult"
titanic.loc[titanic["Age"]<20, "Age_group"]="Child"
print(titanic)

# 데이터 프레임의 가장 마지막 인덱스 확인 후 행 추가
new_index=len(titanic)
print(new_index) #전체가 몇 행인지 숫자로 나올 것
print(titanic.head())

titanic.loc[new_index]=[992,1,1,"shin", "female", 53,0,0,"Pc123", 50.0, "C123", "s", "USA",63, "adult"]
new_data=pd.DataFrame({
    "Name" : ["Alice", "Bob"],
    "Age" : [22,30],
    "Sex" : ["female", "male"],
    "Survived" : [1,0]
})
titanic=pd.concat([titanic, new_data], ignore_index=True)
print(titanic.tail())

# titanic["Name"].str.startswith("Sa") : 문자열이 데이터가 Sa로 시작하는 자료
#titanic[titanic["Age"].astype(str).str.startswith("2")]
#titanic[titanic["Age"].astype(str).str.startswith("^82")]

#파일저장하는법
# titanic.to_csv("./sample.csv" index=False)
# titanic.to_excel("./sample.xls" index=False)
# print("파일 저장이 완료되었다")




#CSV 열기	pd.read_csv()
필터링	df[조건]
정렬	sort_values()
평균·합계	mean(), sum()
결측치 처리	fillna()
국가별 / 품목별 집계	groupby()