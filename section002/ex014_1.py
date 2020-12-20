import sys
sys.stdin=open('./section002/ex014_1.txt','rt')

n = int(input())
firstInputList=list(map(int,input().split()))

m = int(input())
secondInputList=list(map(int,input().split()))

sumInputList=list(firstInputList+secondInputList)
sumInputList.sort()

for k in sumInputList :
    print(k,end=' ')

    