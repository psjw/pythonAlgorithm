import sys

sys.stdin = open('./section001/ex001/ex001_1.txt','rt')
#sys.stdin = open('./section001/ex001/ex001_2.txt','rt')
#sys.stdin = open('./section001/ex001/ex001_3.txt','rt')
#sys.stdin = open('./section001/ex001/ex001_4.txt','rt')
#sys.stdin = open('./section001/ex001/ex001_5.txt','rt')
#sys.stdin = open('./section001/ex001/ex001_6.txt','rt')

n, k = map(int,input().split())

result=[]
for i in range(1,n+1) :
    if n%i==0 :
        result.append(i)
        
if len(result) <= (k-1) :
    print(-1)
else :
    print(result[k-1])
    