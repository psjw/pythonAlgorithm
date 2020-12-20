import sys

sys.stdin=open('ex009_1.txt','rt')
n = int(input())

def sumMoney(x) :
    tempMoney=0
    cnt = 0    
    value = 0
    x.sort()
    tempSet = set(x)
        
    maxValue=x[len(x)-1]
    #print(tempSet)
    for k in tempSet :        
        if cnt < x.count(k) :
            cnt=x.count(k)
            value=k

    if cnt == 1 :
        tempMoney=maxValue*100
    elif cnt == 2 :            
        tempMoney=1000+(value*100)
    elif cnt == 3 :
        tempMoney=10000+(value*1000)        
    return tempMoney

maxSum = -2147000000

for testCase in range(0,n) :
    inputList=list(map(int,input().split()))
    tempSum =sumMoney(inputList)
    if(tempSum>maxSum):
        maxSum=tempSum
   
print(maxSum)  
    
