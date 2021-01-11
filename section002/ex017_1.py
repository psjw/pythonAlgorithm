import sys
sys.stdin=open('./section002/ex017.txt')
n=int(input())
#print(n)
inputList=[[int(x) for x in input().split()] for _ in range(n)]
# print(inputList)

divide= (n//2)
cnt = n-1
leftIdx = divide
rightIdx = divide
tempSum = 0
for i in range(divide+1):    
    # print(" // i : ",i)
    if(leftIdx==rightIdx) :
        tempSum+=inputList[i][leftIdx]
        tempSum+=inputList[i+cnt][leftIdx]
        # print("i : ",i," 1 : ",inputList[i][leftIdx], " 2: " ,inputList[i+cnt][leftIdx])
    else :
        for j in range(leftIdx,rightIdx+1) :        
            tempSum+=inputList[i][j]
            if cnt != 0 :
                tempSum+=inputList[i+cnt][j]
            # print("i : ",i," 3 : ",inputList[i][j], " 4: ",inputList[i+cnt][j])


    
    
    # print("cnt: ",cnt," idx ",i," tempSum : ",tempSum)
    cnt-=2         
    leftIdx-=1
    rightIdx+=1

print(tempSum)