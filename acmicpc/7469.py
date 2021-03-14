import sys
# sys.stdin = open('./acmicpc/7469.txt','rt')
n, m = map(int,input().split())
# print(n,m)
inputList = list(map(int,input().split()))
# print(inputList)
resultList = list()
for s in range(m):
    i,j,k =  map(int,input().split())
    # print(i,j,k)
    
    resultList=sorted(inputList[i-1:j])
    print(resultList[k-1])
