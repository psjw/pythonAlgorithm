import sys
sys.stdin=open("./acmicpc/1037.txt",'rt')

n,k=map(int,input().split())


result=list()
#range(n+1) 하면 0부터 나오니깐 1로 세팅
for i in range(1,n+1) :
    if(n%i == 0) :
        result.append(i)


if len(result)>0 and len(result) > (k-1) :
    print(result[k-1])
else :
    print(0)


