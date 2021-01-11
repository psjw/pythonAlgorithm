import sys
sys.stdin=open('./section002/ex015.txt','rt')
n,m =map(int,input().split())
inputList=list(map(int,input().split()))

count=0
leftp=0
rightp=1
tempSum=inputList[leftp]
while True :
    if tempSum<m :
        if rightp<n:
            tempSum+=inputList[rightp]
            rightp+=1
        else : # rightp가 n이랑 같음
            break
    elif tempSum == m :
        count+=1        
        tempSum-=inputList[leftp]
        leftp+=1
    else : #tempSum > m
        tempSum-=inputList[leftp]
        leftp+=1
        
        
    

    
print(count)    
    

