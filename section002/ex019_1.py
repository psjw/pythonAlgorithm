import sys
sys.stdin=open('./section002/ex019.txt','rt')
n = int(input())

inputList=[list(map(int,input().split())) for _ in range(n)]

#상하 좌우
# i, j
# 상 : i+1 , 하 : i-1 , 좌 : j-1, 우 : j+1
resCnt=0
for i in range(n) :
       
    for j in range(n) :
        cnt =0 
        # print(i,j)
        oriValue=inputList[i][j]                
        if i+1 > n-1 :        
            cnt+=1
        elif oriValue > inputList[i+1][j]   :
            cnt+=1
            
        if i-1 < 0 :
            cnt+=1            
        elif oriValue > inputList[i-1][j] :
            cnt+=1
            
        if j+1 > n-1 :
            cnt+=1
        elif oriValue > inputList[i][j+1]  :
            cnt+=1
            
        if j-1 < 0 :
            cnt+=1
        elif oriValue > inputList[i][j-1] :
            cnt+=1
            
        if cnt==4 :
            resCnt+=1
    

print(resCnt)        
            
                    
