import sys
from collections import Counter
sys.stdin=open('ex005.txt','rt')

n, m =map(int,input().split())


reusltValue=[]

for i in range(1,n+1) :
    for j in range(1,m+1):
        reusltValue.append(i+j)

resultCnt = Counter(reusltValue)


resultList=[]
tempMaxCnt = -2147000000
for k in resultCnt.most_common() :
    if(tempMaxCnt<=k[1]):
        tempMaxCnt=k[1]
        resultList.append(k[0])
    else :
        break
for z in resultList :
    print(z, end=' ')
print()
    