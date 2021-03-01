
# inputList=[x for x in input().strip().split(' ')]
# print(inputList)
import sys

sys.stdin=open('./section001/ex002/ex002_6.txt','rt')

testCase =int(input())

for testCnt in range (1,testCase+1) :    
    n,s,e,k= map(int,input().split())
    inputList=list(map(int, input().split()))    
    resultList=inputList[s-1:e]    
    resultList=sorted(resultList)    
    print("#%d %d"%(testCnt ,resultList[k-1]))
    
    





