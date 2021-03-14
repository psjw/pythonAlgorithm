import sys
import timeit


sys.stdin = open('./company/3_1/3_1_1.txt')

n = int(input())



#상근이 -> 창영이
# 3 or 1개
# 4개 있으면 4-1 = 3/ 4-3 =1  패배
# 3개 있으면 3-3 = 0 승리
# 2개 있으면 2-1 = 1 패배
# 1개 있으면 1-1 = 0 승리
# 짝수 패배, 홀수 승리


if  n % 2 == 0 :
    print("CY")
else : 
    print("SK")
    




    
    
    