import sys
sys.stdin=open('./section002/ex011_1.txt','rt')
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    #print(s[::-1]) #거꾸로 출력됨
    if s==s[::-1]:
        print("#%d YES"%(i+1))
    else :
        print("#%d NO"%(i+1))