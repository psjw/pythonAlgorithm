import sys

sys.stdin=open('./section001/ex004/ex004_6.txt','rt')

n = int(input())
inputList = list(map(int,input().split()))

meanScore = round(sum(inputList)/n)
print(meanScore)
temp = 0
lowValue = 4999
index = 0
for i in range(n) :    
    temp = round(abs(inputList[i]-meanScore))
    if lowValue > temp :        
        lowValue = temp
        index=i
    elif lowValue ==  temp :
        if inputList[i] > inputList[index] :                        
            lowValue = temp           
            index=i
        
   
   
print("%d %d"%(meanScore,index+1))
