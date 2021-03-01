import sys
import time
sys.stdin=open('./section001/ex007/ex007_6.txt','rt')

n = int(input())
print(n)



divideList=[0]*(n+1)
cnt=0
# print(divideList)
start = time.time()
for i in range(2,n+1):  
    if divideList[i]==0 :
        cnt+=1
        for j in range(i,n+1,i) :   
            divideList[j]=1
print("time : ",time.time()-start)
print(cnt)