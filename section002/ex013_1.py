import sys
import copy
sys.stdin=open('./section002/ex013_1.txt','rt')
# a,b= map(int,input().split())
# a, b= b,a

#inputList=[x for x in range(1,21)]
a = list(range(21))
for _ in range(10) : # _ 변수가 없다 변수의 대입 없이 반복
    s, e =map(int, input().split())    
    s, e = e, s  
    # print('//~',s,e)
    idx=s-e # 10-5 :5
    # print("init :",idx)
    tempList=copy.deepcopy(a)   
    # print(tempList)
    for i in range(s, e-1 , -1 ):        
        # 10-5 :5
        # 10-4 : 6
        # 10-3 : 7
        # 10-2 : 8
        # 10-1 : 9
        # 10-0 : 10
        #print(i,idx,s-idx)        
        #print(s-idx,s,idx, i, tempList[i])
        a[s-idx]=tempList[i]    
        #print(a)
        idx-=1
        

for i  in range(1,21) : 
    print(a[i],end=' ')
print()