
# inputList=[x for x in input().strip().split(' ')]
# print(inputList)

import sys
# rt 읽기 / 텍스트모드
sys.stdin=open('ex2.txt','rt')

testCase=int(input())

# testCase = int(input().strip())

for testCnt in range(1,testCase+1) :
    # 0 : 갯수 , 1 ~ 2 : 범위 , 3 : 출력자리     
    #inputEnv=[int(x) for x in input().strip().split(' ')]
    n, s, e, k = map(int,input().split())
    # print(inputEnv, end='\n')
    inputList = list(map(int,input().split()))
    #inputList = [int(x) for x in input().strip().split(' ')]
    # resultList=[]
    startIdx=s-1
    endIdx =e
    resultList=inputList[startIdx:endIdx]
    # for i in range(startIdx,endIdx):
    #     resultList.append(inputList[i])
  

    # sort 원래 List를 정렬 시킴
    #inputList.sort() 
    #print(inputList,end='\n')
    # sorted(inputList) 원래 List는 건들이지 않음   
    searchIdx=k-1
    # print(sorted(resultList)) 
    print('#%d %d'%(testCnt,sorted(resultList)[searchIdx]))