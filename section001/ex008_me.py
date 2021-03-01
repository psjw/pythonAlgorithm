import sys

sys.stdin=open('./section001/ex008/ex008_5.txt','rt')

n =int(input())

inputList = list(map(int,input().split()))

def isPrime(x):    
    isResult=True
    if x == 1 :
        isResult = False
    for k in range(2,x) :
        if x%k == 0 :
            isResult = False
            break
    return isResult

def reverse(x) :
    inputStr=str(x)
    result=""
    for i in range (1,len(inputStr)+1) :     
        divided=x%10
        x=x//10
        if divided > 0 :
            result+=str(divided)
    return int(result)




resultList=[]
for k in range(n):
    temp=reverse(inputList[k])
    if(isPrime(temp)):
        print(temp, end=' ')
print()

