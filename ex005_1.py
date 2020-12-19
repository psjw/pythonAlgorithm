import sys
sys.stdin=open('ex005.txt','rt')

n, m =map(int,input().split())

resultCnt=[0]*(n+m+3)

for i in range(1,n+1) :
    for j in range(1,m+1):        
        resultCnt[i+j]+=1;
print(resultCnt)
max = -2147000000
for k in range(1,n+m+1):
    if resultCnt[k]>max:
        max=resultCnt[k]

for z in range(1,n+m+1):
    if resultCnt[z]==max :        
        print(z, end=' ')
