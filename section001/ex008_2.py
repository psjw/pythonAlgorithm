import sys
#sys.stdin = open('ex008_1.txt','rt')
n=int(input())
a=list(map(int,input().split()))

def reverse(x):
    res=0
    # x = 9010
    while x>0:
        t=x%10 # 9010 % 10=0 -> 901 % 10 = 1
        res=res*10+t # 0*10+0=0 ->  0*10+1=1 -> 1*10+0=10 -> 10*10+9=109
        x=x//10 # 9010 // 10 = 901 -> 901 // 10 = 90 -> 90//10=9 -> 9//10=0
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1) : # 1* 16 -> 2 * 8 절반까지만 존재 
        if x%i==0:
            return False
    else :
        return True    
    
for x in a:
    tmp=reverse(x)
    if isPrime(tmp) :
        print(tmp,end=' ')