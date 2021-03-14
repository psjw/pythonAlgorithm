import sys
sys.stdin=open('./section002/ex018.txt','rt')
n = int(input())
inputList = [[int(x) for x in input().split()] for _ in range(n)]
m = int(input())
orderList = [[int(x) for x in input().split()] for _ in range(m)]

# print(inputList)
# print(orderList)
moveIdx=0
for i in range(m):
    rowList=[0]*n
    row, direction, move = orderList[i]
    # print(row, direction, move)
    for j in range(n) :        
        if(direction == 0) : #왼쪽
            moveIdx=j-move                        
        else :
            moveIdx=j+move
        if moveIdx < 0 :
            moveIdx+=n
        else :
            moveIdx-=n
        # print(row,j,m,moveIdx)
        rowList[moveIdx]=inputList[row-1][j]   
        
            
        
        
    inputList[row-1]=rowList
    # print(inputList)
s=0
e=n-1
res=0
# print(n//2+1 )
for i in range(n):
    for j in range(s,e+1):
        
        res+=inputList[i][j]
        # print(i,j,s,e,res,inputList[i][j])
    
    if i < n//2 :
        s+=1
        e-=1
    else :
        s-=1
        e+=1

print(res)

