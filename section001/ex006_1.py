import sys
sys.stdin=open('ex006_1.txt','rt')
n = int(input())



inputList = list(map(int,input().split()))


def digit_sum(x):
    lastIdx=len(str(x))
    tempSum=0
    # print(idx,i)
    # print("lastIndx : ",lastIdx)
    for j in range(lastIdx,0,-1):
        # print(j, len(str(i)))
        # print("i: ",i,"j : ",j)
        if j == 1 :
            # print("나머지 : ",i%10)
            tempSum+=i%10
            
        else :
            # print(j)
            # print("몫 : ", i//(10**(j-1)))
            # print("/// : ",j)
            divide=x//(10**(j-1))                                    
            tempSum+=(divide)
            x-=(divide*(10**(j-1)))                                    
    return tempSum

    

# print(inputList)
resultMaxValue=-2147000000
resultIdx=0;
for idx,i in enumerate(inputList) :
    tempSum = digit_sum(i)                                      
    if tempSum>resultMaxValue :
        resultMaxValue=tempSum
        resultIdx=idx
print(inputList[resultIdx])

