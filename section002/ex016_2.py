import sys
sys.stdin=open('./section002/ex016.txt','rt')
n=int(input())
#a=[list(map(int,input().split()))] #한줄을 읽어서 리스트화 시킴 -> [[10, 13, 10, 12, 15]]

a=[list(map(int,input().split())) for _ in range(n)] 
#print(a)

largest = -2147000000

for i in range(n):
    sum1=sum2=0#sum1 행의 합 , sum2 열의합
    for j in range(n):
        sum1+=a[i][j] # 행
        sum2+=a[j][i] # 열
    if sum1>largest:
        largest =sum1
    if sum2>largest:
        largest =sum1

sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][(n-1)-i]

if sum1>largest:
    largest =sum1
if sum2>largest:
    largest =sum1
    
print(largest)