import sys
sys.stdin=open('ex011_1.txt','rt')
n=int(input())

inputList=list()
print(n)
reverseStr="a"
inputStr=""
for i in range(0,n) :            
    inputList=list(map(str,input().lower()))
    reverseList=reversed(inputList)
    inputStr=[x for x in inputList]
    inputStr="".join(inputList)
    reverseStr="".join(reverseList)
    if inputStr == reverseStr :
        print("#%d YES"%(i+1))
    else :
        print("#%d NO"%(i+1))
    