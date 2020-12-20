import sys
sys.stdin=open('./section002/ex014_1.txt','rt')

n = int(input())
firstInputList=list(map(int,input().split()))

m = int(input())
secondInputList=list(map(int,input().split()))

point1 = 0
point2 = 0

maxlength = len(firstInputList)

if len(secondInputList)>maxlength : 
    maxlength= len(secondInputList)
    
resultList=list()


for i in range(maxlength) :
    print(point1,point2)
    if firstInputList[point1] == secondInputList[point2] :
        resultList.append(firstInputList[point1])
        point1+=1
        point2+=1
    elif firstInputList[point1] < secondInputList[point2] :
        resultList.append(firstInputList[point1])
        point1+=1
    else :
        resultList.append(secondInputList[point2])
        point2+=1
    if point1 > len(firstInputList)-1 :
        for k in range(point2,len(secondInputList)):
            resultList.append(secondInputList[k])
        break
    elif point2 > len(secondInputList)-1 :
        for k in range(point2,len(firstInputList)):
            resultList.append(firstInputList[k])
        break



print(resultList)