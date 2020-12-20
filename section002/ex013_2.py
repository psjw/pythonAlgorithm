import sys
import copy
sys.stdin=open('./section002/ex013_1.txt','rt')
# a,b= map(int,input().split())
# a, b= b,a

a = list(range(21))
for _ in range(10) : # _ 변수가 없다 변수의 대입 없이 반복
    s, e =map(int, input().split())    
    # 2 ~ 7  (7-2+1)//2 =3 -> (e-s+1)// 2 -> 포문 
    for i in range((e-s+1)//2) :
        a[s+i],a[e-i] = a[e-i],a[s+i]

a.pop(0)
for x in a :
    print(x,end=' ')