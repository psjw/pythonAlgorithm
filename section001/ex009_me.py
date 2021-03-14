import sys

sys.stdin=open('./section001/ex009/ex009_1.txt')

n = int(input())

def sumMoney(x) :
    
    cnt=0
    tempSet=set(x)
    print(tempSet)
    tempList=list(tempSet)
    tempList.sort()
    for k in range(len(tempList)) :       
        print(x.count(tempList[k]))
        cnt=x.count(tempList[k])
        
        if cnt
        


for i in range(n):    
    inputList=list(map(int,input().split()))
    print(inputList)
    sumMoney(inputList)








