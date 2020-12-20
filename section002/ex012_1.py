import sys
sys.stdin=open('./section002/ex012_1.txt','rt')
m=list((input()))

temp=""
for i in m :
    if i.isdigit() :
        temp+=i

print(int(temp))
tempInt=int(temp)
cnt=1 #자기 자신포험
for k in range(1, tempInt//2+1) : # tempInt//2+1 -> 2로 나눈 후 1을 더함
    if tempInt%k == 0 :
        #print(k)
        cnt+=1

print(cnt)




