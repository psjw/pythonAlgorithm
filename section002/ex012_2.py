import sys
sys.stdin=open('./section002/ex012_1.txt','r')
s=input()
res=0
for x in s :
    #print(x,end=' ')
    # print(x, x.isdecimal())
    if x.isdecimal() : # isdigit() : 2^2 같은 것도 인식  / isdecimal() :  0~9까지만 인식
        res = res*10+int(x)
print(res)        

cnt =0 
for i in range(1, res+1):
    if res%i == 0 :
        cnt+=1

print(cnt)


