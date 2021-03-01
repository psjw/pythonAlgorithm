import sys
sys.stdin=open('./section001/ex001/ex001_1.txt','rt')
n, k = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    if n%i == 0 :
        cnt+=1
    if cnt == k :
        print(i)
        break
else : #break 시에는 else로 오지 않음
    print(-1)



