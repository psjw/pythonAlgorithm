import sys

sys.stdin=open('./section001/ex007/ex007_6.txt','rt')
n = int(input())

result=[0]*(n+1)


result[1]=1
cnt=0
for  i in range(2,n+1):
    if(result[i]==0):
        cnt+=1
        for j in range(i,n+1,i) :
            result[j]=1

print(cnt)