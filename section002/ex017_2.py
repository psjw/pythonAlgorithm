import sys
sys.stdin=open('./section002/ex017.txt')
n=int(input())
#print(n)
a=[list(map(int,input().split())) for _ in range(n)]
print(a)
res=0
s=e=n//2

for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i <n//2 :
        s-=1
        e+=1
    else :
        s+=1
        e-=1
print(res)    
    
