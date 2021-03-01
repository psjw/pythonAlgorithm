import sys

sys.stdin = open('./section001/ex006/ex006_6.txt','rt')

n = int(input())
inputList=list(map(int,input().split()))



def digit_sum(x) :
    result=0
    for i in range(1,len(str(x))+1):             
        result+=x%10
        x=round((x-(x%10))/10)        
    return result


result=0
cnt=0

for j in range(n) :
    temp=digit_sum(inputList[j])    
    if result<temp :     
        result=temp   
        cnt=j

print(inputList[cnt])

        



