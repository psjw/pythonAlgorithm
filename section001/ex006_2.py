import sys
sys.stdin=open('ex006_1.txt','rt')
n=int(input())
a=list(map(int,input().split()))

def digit_sum(x):
    sum=0
    while x>0:# 125 -> 12 -> 1
        sum+=x%10 # 5 -> 2 -> 1 
        x=x//10 #12 -> 1
    return sum
    
max = -2147000000
    
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
        
print(res)