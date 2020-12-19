# import sys
# sys.stdin=open("input.txt",'rt')



# a,b= input().strip().split(' ')
# print('a = ',a,' / b = ',b)

# inputList = [int(x) for x in input().strip().split(' ')]

# a = inputList[0]
# b = inputList[1]

import sys
#sys.stdin=open('ex001.txt','rt')
a, b=map(int,input().split())


result = []
cnt = 0

for i in range(1, a+1):
    if a%i == 0 :
        cnt+=1
    if cnt == b:
        print(i)
        break
else : # break시에는 else 쪽으로 오지 않음    
    print(-1)



