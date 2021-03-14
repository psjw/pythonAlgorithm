# 시간초과 소스
import sys
sys.stdin=open('./section002/ex015.txt','rt')
n,m =map(int,input().split())
inputList=list(map(int,input().split()))

count=0

for i in range(0,n) :
    # 만약에 현재 List 요소 하나의 값이 m이랑 같으면 countinue
    if inputList[i] == m :
        count+=1        
        continue
    
    # 만약에 현재 List요소가 m보다 크면 더해서 나올수 없으므로 Continue
    elif inputList[i] > m :        
        continue
    
    # 요소들의 합을 구해야 한다면 for문 돌린다.
    # 초기 값은 현재 i의 값으로 해준다
    tempSum=inputList[i]
    # i보다 1개의 인덱스가 큰 값으로 해줘서 다음 값부터 덧셈을 구한다
    for j in range(i+1, n):
        tempSum+=inputList[j]        
        if tempSum == m :
            count+=1            
            break
        # 합이 초과 하면 더이상 더해도 의미없다.
        elif tempSum > m :            
            break
    
print(count)
