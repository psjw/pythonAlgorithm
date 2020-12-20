import sys
sys.stdin=open('ex010_1.txt','rt')

n=int(input())


inputList=list(map(int,input().split()))

resultList=[0]*n


for i in range(0,n) :
    #초기값 세팅
    if i == 0 and inputList[i] == 1 :
        resultList[i]=1
    elif resultList[i-1] == 0 and inputList[i] == 1 :
        resultList[i] =1
    elif resultList[i-1] >0 and inputList[i] == 1 :
        resultList[i] = resultList[i-1]+1

print(sum(resultList))
