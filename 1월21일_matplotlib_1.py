import matplotlib.pyplot as plt

#하나의 숫자 리스트 입력 y축값!!!!!!!!!!!!!!!!!!!
plt.plot([2,3,4,5])  
plt.show()  #run 시키면 그래프 뜬다잉

plt.plot([1,2,3,4], [1,4,9,16])  #첫번째 x축, 두번째 y축. 꺾이는 지점 좌표
plt.xlabel("X-label")  #축 이름 지정. 라벨
plt.ylabel("Y-label") 
plt.show()

plt.plot([1,2,3,4], [1,4,7,9], label="Square") #그래프 이름 . 라벨
plt.xlabel("X-label") 
plt.ylabel("Y-label") 
plt.legend() #a small box that explains what each line, color, or marker on the plot represents 
plt.show()


#xlim(xmin, xmax)
#ylim(ymin, ymax)
plt.plot([1,2,3,4], [3,6,9,12])
plt.xlabel("X-label") 
plt.ylabel("Y-label") 
plt.xlim([0, 5])
plt.ylim([0, 15])
#아니면 두 줄 대신 plt.axis([0, 5],[0, 15])
plt.show()


#선종류 solid line, dashed line(짧은실선), dash-dot line(점선실선반복), dotted line(점선)
plt.plot([1,2,3], [4,4,4], "-", label="solid", color="#ff7f00")    #따옴표 기호로 쓰거나
plt.plot([1,2,3], [3,3,3], "--", label="dashed", color="red")

plt.plot([1,2,3], [2,2,2], linestyle="dotted", label="dotted", color="blue")  #따옴표 명칭 쓰거나
plt.plot([1,2,3], [1,1,1], linestyle="dashdot", label="dash-dot", color="green") 

plt.xlabel("X-label") 
plt.ylabel("Y-label") 

plt.legend(loc="upper right", ncol=4) #오른쪽 위에 라벨 띄우기. 4개 컬럼으로
plt.show()



#마커 Marker : 데이터 지점(point) 표시 'o', 's'	,'D','d','p', 'h', '^', 'v'	, '<' ,'>'
plt.plot([4,5,6], "b" )  
plt.plot([3,4,5], "ro" )
plt.plot([2,3,4], marker="s" )
plt.plot([1,2,3], marker="D" ) 
plt.plot([0,1,2], marker="$A$" )   
plt.title("titanic", loc="center", pad=10) #padding 제목과 그래프 사이 간격  
plt.show()

#color : b,g,r,c,m,y,k(black),w     #붙이고 기타 16진수 색상


#산점도 차트 scatter plot
import numpy as np 
np.random.seed(0) #seed : 코드를 실행할때마다 매번 '똑같은 랜덤 값'을 고정 
n=50
x=np.random.rand(n) #0~1   random: rand라는 메소드를 쓰겠다. rand() : 난수발생
y=np.random.rand(n) #0~1

size = (np.random.rand(n)*20)**2
color = np.random.rand(n)
plt.scatter(x,y, s=size, c=color, alpha=0.5)  #alpha 0에서 1사이 투명도
plt.colorbar()
plt.show()