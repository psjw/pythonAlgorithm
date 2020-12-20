import sys
sys.stdin=open('./section002/ex011_1.txt','rt')
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    # -5 -4 -3 -2 -1
    #   0 1 2 3 4 
    #s: l e v e l
    # 5//2 = 2
    # s[j]!=s[-1-j] 0 , -1 /  1, -2
    #print(s[-1])
    for j in range(size//2) : 
        if s[j]!=s[-1-j] :
            print("#%d NO"%(i+1))
            break
    else :
        print("#%d YES"%(i+1))
