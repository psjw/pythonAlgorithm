import sys
sys.stdin=open('ex003.txt','rt')
n,k=map(int,input().split())

a=list(map(int,input().split()))
result=set()

for i in range(n):
    for j in range(i+1,n): 
        for m in range(j+1,n) :          
            result.add(a[i]+a[j]+a[m])

result=list(result)
result.sort(reverse=True)
print(result[k-1])
#print(sorted(result)[len(result)-k])    