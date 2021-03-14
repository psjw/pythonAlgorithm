import sys

sys.stdin=open('./1700.txt')

#구멍갯수 N (1 ≤ N ≤ 100)
#사용횟수  K (1 ≤ K ≤ 100)
#전기용품의 이름이 K 이하
n, k = map(int,input().split())


a = list(map(int,input().split()))


elect = [0] * (k+1)

#print(n,k)
#print(a)



concentList=[]

cnt=0
#print(a)
for i in range(k) :
    if a[i] in concentList : #있으면 Pass
            continue       
    elif len(concentList) < n : #최초
        #print("@")
        concentList.append(a[i])                     
        continue
         
    #없으면 콘센트리스트에서 확인  
    index, maxConcent=-1,-1
    for j in range(n):
        #print(i,a[i], concentList[j],a[i:],concentList)
        if concentList[j] not in a[i:] : #콘센트가 없으면 체인지
            #print("step1")
            concentList[j]=a[i]
            cnt+=1
            break
        elif maxConcent < a[i:].index(concentList[j]) : #콘센트가 가장 멀리 있는것 부터 제거
            #print("step2 : "+str(j)+" / "+str( a[i:].index(concentList[j])))
            maxConcent=a[i:].index(concentList[j])
            index = j                
        
    else :
        #print("index : "+str(index))
        if index>-1 :
            concentList[index]=a[i]
            cnt+=1
    
    
        
#print(elect)
#print(concentList)
print(cnt)
        



