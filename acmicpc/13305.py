import sys

sys.stdin=open('./13305.txt','rt')

n = int(input())


costList = list(map(int,input().split()))

cityList = list(map(int,input().split()))

cost = cityList[0]*costList[0]

cityCnt=1
minCityCost=cityList[0]

while cityCnt < n-1 :
    #print(cityList[cityCnt] , cityList[cityCnt-1] ,cityCnt)
    if minCityCost > cityList[cityCnt] :               
        minCityCost = cityList[cityCnt]
    #print(costList[cityCnt],minCityCost)
    cost+=costList[cityCnt]*minCityCost
    cityCnt+=1
    #print(cost)



        
print(cost)    
    