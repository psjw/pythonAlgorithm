import sys
import math
sys.stdin=open('ex004.txt','rt')

n = input().split()
result=list(map(int,input().split()))
# 올림 math.ceil
# 내림 math.trunc
#     math.floor
# 반올림 round

avg=round(sum(result)/n)

resultMinus=[abs(i-avg) for i in result]
resultIndex=[x for x in range(len(resultMinus)) if abs(resultMinus[x])==min(resultMinus)]
resultValue=[result[z] for z in resultIndex]
print(avg,result.index(max(resultValue))+1)


#print(list(filter(lambda x:abs(resultMinus[x])==1, range(len(resultMinus)))))


        
        

