import sys
import timeit


sys.stdin= open('./company/3_1/3_1_2.txt')

n =int(input()) #좌석 개수
m =int(input()) #고정석 개수

vipList=[] #고정석 번호

for mCnt in range(m):
    vipList.append(int(input()))    

start_time = timeit.default_timer() # 시작 시간 체크
seatList=[]
seatList.append(0)  #0 번         
seatList.append(1)  #1자리    
seatList.append(2)  #2자리   

for j in range(3,n+1):
    seatList.append(seatList[j-1]+seatList[j-2])


preIdx=0
result=1
for i in range (0,m) :
    result = result*seatList[vipList[i]-1-preIdx]
    preIdx = vipList[i]
else :
    result = result*seatList[n-preIdx] #마지막줄    
#print(seatList)

if m < 1 :
    result= seatList[n]
    
print(result)
terminate_time = timeit.default_timer() # 종료 시간 체크 

print("%f초 걸렸습니다." % (terminate_time - start_time))




        