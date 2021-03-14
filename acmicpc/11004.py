import sys
sys.stdin = open('./acmicpc/11004.txt','rt')
n, k = map(int,input().split())
# print(n,k)
inputList = list(map(int,input().split()))
# print(inputList)

inputList.sort()
print(inputList)
print(inputList[k-1])