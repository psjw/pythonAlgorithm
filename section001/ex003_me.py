import sys
sys.stdin=open('./section001/ex003/ex003_6.txt','rt')

n, k  = map(int,input().split())

inputList = list(map(int,input().split()))
resultSet = set()

for i in range (n) :
    for j in range(i+1, n) :
        for m in range(j+1, n):
            resultSet.add(inputList[i]+inputList[j]+inputList[m]) 

resultList=list(resultSet)
resultList.sort(reverse=True)
print(resultList[k-1])
