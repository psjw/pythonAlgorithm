import sys

sys.stdin = open('./section001/ex005/ex005_6.txt','rt')

n, m = map(int,input().split())


resultList=[0]*(n+m+1)
print(resultList)


        
for i in range(1,n+1):
    for j in range (1,m+1):
        resultList[i+j]+=1


max=0



for k in range(n+m):    
    if max < resultList[k] :
        max=resultList[k]


for m in range(n+m+1) :
    if resultList[m]==max :
        print(m,end=' ')
print()