import sys
sys.stdin=open('./acmicpc/1037.txt','rt')
n, k =map(int,input().split())

count = 0
result = 0
for i in range(1,n+1) :
    if n%i == 0 :
        count+=1
    # 만약 i와 k가 같다면 break로 빠져나온다    
    # 만약 k가 count보다 크다면 break로 빠져나오지 않는다.
    if count == k :                
        result=i
        break


print(result)