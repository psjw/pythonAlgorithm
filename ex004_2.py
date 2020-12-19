import sys
sys.stdin=open('ex004.txt','rt')
n=int(input())
a=list(map(int,input().split()))
ave=round(sum(a)/n) #rouud는 round_half_even 방식을 택한다. ->round_half_up방식이 아님
min=2147000000
for idx, x  in enumerate(a):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp == min :
        if x>score :
            score=x
            res=idx+1



print(ave,x)