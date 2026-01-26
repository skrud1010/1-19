import numpy as np 
#선형대수 연산에 필요한 다차원 배열과 연산을 수행하는 다양한 함수 제공

#1. 넘파이 배열
# 파이썬 리스트와 비슷해 보이지만 계산 속도가 훨씬 빠르다

a_values=np.array([12500,45000,32000,0,56000])
print(a_values)  #1행 

b_values=np.array([
    [1000,2000,3000,4000],
    [5000,6000,7000,8000],
    [10000,11000,12000,13000]
])  
print(b_values)  #3행 4열

c_values = np.array([
    [#지역이 아시아
        [100,200,300],
        [200,300,400],
        [500,600,700]
    ],
    [#유럽
        [90,80,50],
        [80,80,40],
        [100,80,90]
    ],
    [#북유럽
        [190,880,50],
        [80,100,30],
        [100,60,110]
    ]
])
print(c_values)  #너비까지 생겼따

print(a_values.shape)  #(5,) 행열 모양
print(b_values.shape)  #(3, 4)
print(c_values.shape)  #(3, 3, 3)

print(a_values.itemsize)  #자료구조  8byte
print(b_values.itemsize)  #8
print(c_values.itemsize)  #8

print(a_values.size)  #5
print(b_values.size)  #3*4=12
print(c_values.size)  #3*3*3=27
 
#np.zeros : 0으로 구성된 N차원 배열 생성
#np.ones : 1으로 구성된 N차원 배열 생성
#np.empty : 초기화 되지 않는 N차원 배열 생성

print(np.zeros((4,6)))
print(np.ones((2,3,4), dtype=np.int64))
print(np.empty((2,3)))
print(np.arange(10,30,5)) #[10,15,20,25]
print(np.arange(0, 2, 0.3)) #[0., 0.3, 0.6, 0.9, 1.2, 1.5, 1.8]

print(np.linspace(0, 99 ,100))    #0부터 99까지 1씩(등분)
print(np.arange(0, 1+0.25, 0.25)) #[0.   0.25 0.5  0.75 1.  ]
print(np.linspace(0,1,5))       #[0.   0.25 0.5  0.75 1.  ]
 
a=np.arange(6)
print(a)
b=np.arange(12).reshape(4,3)
print(b)
c=np.arange(24).reshape(2,3,4)
print(c)

a=np.array([20,30,40,50])
b=np.arange(4)
c=a-b
print(c) #[20 29 38 47]

print(b*10)  #[ 0 10 20 30]

print(a<35) # [ True  True False False]

A = np.array([
    [1,1],
    [0,1]
])

B = np.array([
    [2,0],
    [3,4]
])

print(A * B)    # 2, 0, 0, 4
print(A @ B)    #행렬 곱셈





#1월21일

#int < float 
# .sum 합
# .min 최솟값
# .max 최대값
# .argmax 모든 요소 중 최대값의 인덱스
# .cumsum 모든 요소 누적합
a= np.arange (8).reshape(2,4)**2    #0부터 7까지, 2열 4행, 각 요소의 제곱
print(a)  #[[ 0  1  4  9]   [16 25 36 49]]
print(a.sum())  #140
print(a.min())  #0
print(a.argmax())  #7(번째임)  
print(a.cumsum()) # [  0   1   5  14    30  55  91 140]

#축기준 axis=0 열 기준    axis =1 행기준
b=np.arange(12).reshape(3,4)
print(b) #[[ 0  1  2  3]  [ 4  5  6  7]  [ 8  9 10 11]]
print(b.sum(axis=0))   #열기준으로(열끼리) 합을 내겠다 [12 15 18 21]
print(b.sum(axis=1))   #행기준으로 합  [ 6 22 38]

#인덱싱 슬라이싱
a=np.arange(10)**2   #0부터 9까지, 각 요소들 제곱함
print(a)  #[ 0  1  4  9 16 25 36 49 64 81]
print(a[2])  #4
print(a[2:5]) #4 9 16
a[0:6:2]=1000
print(a) #0 4 16 을 1000으로 바꿔라


a=np.arange(8)**2  #0 1 4 9 15 25 36 49
i=np.array([1,3,3,5])  
print(a[i])  #1, 9,  9, 25

j=np.array([[3,4], [5,6]])
print(a[j]) #9 16     25 36

#1차원으로 변경     .ravel
#.reshape : 지정한 차원으로 변경
#.T : 전치변환 ex) 2,3->3,2 차원을 바꾼다
a=np.arange(12).reshape(3,4)
print(a.shape)  #3,4
print(a.ravel()) #[ 0  1  2  3  4  5 6  7  8  9 10 11]
print(a.shape)  #3,4

print(a.reshape(2,6))  #[[ 0  1  2  3  4  5]    [ 6  7  8  9 10 11]]
print(a.shape)  #(3, 4)
print(a.T)  #[[ 0  4  8]   [ 1  5  9]   [ 2  6 10]   [ 3  7 11]]
print(a.T.shape)  #(4, 3)



#np.stack
#np.hstack : axis=1행 쌓기

#np.hsplit :숫자1개가 들어가면 x개로 등분
#np.hsplit : 리스트를 넣을 경우 X 기준으로 데이터 분할

a=np.arange(12).reshape(2,6) #0 1 2 3 4 5  6 7 8 9 10 11
print(np.hsplit(a,3)) #[array([[0, 1], [6, 7]]), array([[2, 3], [8, 9]]), array([[ 4,  5], [10, 11]])]
print(np.hsplit(a,(3,4))) #[array([[0, 1, 2], [6, 7, 8]]), array([[3], [9]]), array([[ 4,  5], [10, 11]])]

b=np.array(np.vstack((a,b)))
print(np.vstack(a,b))
print()