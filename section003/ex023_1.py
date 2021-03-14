import sys
sys.stdin=open('./section003/ex023.txt','rt')
k, n=map(int,input().split())
inputList=[]
for _ in range(k) :
    inputList.append(int(input()))
print(inputList)

lt=0
rt=max(inputList)

res=0
cnt=0

while lt<=rt :
    mid = (lt+rt) // 2
    tempCnt=0
    for i in range(k) :
        tempCnt+=(inputList[i]//mid)
    if tempCnt == n :
        cnt=tempCnt
        res=mid
        break
    elif tempCnt > n :
        lt=mid+1
    else :
        rt=mid-1
        
print(res)
    
    
