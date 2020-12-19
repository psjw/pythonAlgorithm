import sys

sys.stdin=open("ex008_1.txt",'rt')

n=int(input())

inputList = list(map(int, input().split()))
print(inputList)

def isPrime(x):
    cnt=0
    isCheckPrime=True    
    for i in range(2,x):        
        if x%i == 0 :            
            cnt=1
            break
    if cnt>0 :
        isCheckPrime=False
    return isCheckPrime

def reverse(x):
    revereList=list()
    
    for j in range(len(str(x)),0,-1):            
        if j!=1 :            
            divide=x//(10**(j-1))           
            revereList.append(divide)
            # 몫 * 자릿수
            x-=(10**(j-1))*divide            
        else : 
            reminder=x%10               
            revereList.append(reminder)

    
    revereList=list(reversed(revereList))
    tempStr=str()
    for k in revereList :
        tempStr+=str(k)
    
    return int(tempStr)


for i in inputList:
    reverseNumer=reverse(i)
    isCheckPrime=isPrime(reverseNumer)    
    if isCheckPrime :        
        print(reverseNumer,end=' ')
    
print()
    
        

