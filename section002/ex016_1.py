import sys
sys.stdin=open('./section002/ex016.txt','rt')
n = int(input())


#inputList = list()
#for i in range(n):
#    inputList.append(list(map(int,input().split())))
inputList =[[int(x) for x in input().split()] for k in range(n) ]
# print(inputList)
tempSum=-2147000000
result=[0]*4
for i in range(0, n) :    
    for j in range (0, n) :
        result[0]+=inputList[j][i]    # 상 -> 하 의 합
        result[1]+=inputList[i][j]    # 좌 -> 우 의 합    
        # print(result[1], inputList[i][j], i,j)
    if tempSum  <  result[0] or tempSum < result[1] :
        if result[0] > result[1] :
            tempSum =result[0]            
        else:
            tempSum = result[1]
    # print(i, result[0], result[1],tempSum)
    result[0]=0
    result[1]=0
    result[2]+= inputList[i][i] # 좌상 -> 우하 대각
    result[3]+= inputList[i][(n-1)-i] # 우상 -> 좌하 대각
    #print("### ",i, "result[2] : ", result[2], "result[3] : ",result[3])
    if i == n-1 : #마지막 인덱스
        if result[2] > tempSum or result[3] >tempSum :
            if result[2] > result[3] :
                tempSum = result[2]
            else :
                tempSum = result[3]
        
    #print(inputList[i][0]) 상 -> 하
    #print(inputList[i][i]) 좌상 -> 우하 대각
    #print(inputList[i][(n-1)-i]) 우상 -> 좌하 대각
    #print(inputList[0][i]) 좌 -> 우
print(tempSum)