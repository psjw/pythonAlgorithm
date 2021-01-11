import sys
sys.stdin=open('./section003/ex022.txt','rt')
n, m = map(int,input().split())
inputList = list(map(int,input().split()))


inputList.sort()
print(inputList)
idx=-1
lt=0
rt=n-1
mid=(lt+rt)//2
for i in range(n) :    
    if inputList[mid] >  m :
        rt=mid-1
        mid=(lt+rt)//2
    elif inputList[mid] < m :
        lt=mid+1
        mid=(lt+rt)//2
    else :
        idx=i+1
        break
    

print(idx)