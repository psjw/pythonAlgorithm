import sys
sys.stdin=open('./section002/ex021.txt','rt')

inputList=[list(map(int,input().split())) for _ in range(7)]
# print(inputList)
n=7
sp=ep=n//2-1
# print((n//2)*2)
cnt=0
res=0
rowCnt=0
colCnt=0

for i in range(n):        
    idxCnt=0
    cnt=0
    sp=ep=n//2-1
    for j in range((n//2)*2): 
        # print("######",j)  
        # print(sp,ep)     
        sp-=1
        ep+=1
        # print(i,sp,ep)
        if inputList[i][sp] == inputList[i][ep] :            
            rowCnt+=1
        if inputList[sp][i] == inputList[ep][i] :            
            colCnt+=1
        cnt+=1
        # print("rowCnt : ",rowCnt,inputList[i][sp], inputList[i][ep], cnt, res)
        if cnt == 2 :
            if colCnt == 2 :
                res+=1   
            if rowCnt == 2 :
                res+=1 
            cnt=0            
            sp=ep=n//2+idxCnt
            idxCnt+=1
            rowCnt=0
            colCnt=0
 
 
print(res)            

