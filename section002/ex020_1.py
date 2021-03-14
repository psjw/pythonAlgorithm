import sys
sys.stdin=open('./section002/ex020.txt','rt')
n=9
inputList = [list(map(int,input().split())) for _ in range(9)]
# print(inputList)
s = 0
e = 2
res=0
tempSet1 = set()   
tempSet2 = set()   
tempSet3 = set()   
ifCnt= 0

while True :
      
    for i in range(n) :        
        # print("###",i,s,e)
        for j in range(s,e+1) :
            tempSet1.add(inputList[i][j])
        # print(i,j,len(tempSet))
        if len(tempSet1) == 9 and (i+1) % 3 ==0 :
            res+=1
            tempSet1 = set()     
    if ifCnt == 0 :
        for i in range(n) :
            ifCnt+=1
            for j in range(n) :                      
                tempSet2.add(inputList[i][j])
                tempSet3.add(inputList[j][i])
                #print(i,j,len(tempSet2),res)
                #print(i,j,len(tempSet2))
                if j == 8 :
                    print("## ifcnt",ifCnt,i,j)
                    if len(tempSet2) == 9 :
                        res+=1             
                    if len(tempSet3) == 9 :
                        res+=1
                        
                    tempSet2 = set()  
                    tempSet3 =set()
        
    

                    
    
    
    s+=3
    e+=3
    if s > n or e > n :
        break

print(res)
if res == 27 :
    print("YES")
else :
    print("NO")
