# 최솟값 구하기
arr=[5,3,7,8,2,5,2,6]
arrMin=float('inf') #or arr[0]
# for i in range(len(arr)):
    # if arr[i]<arrMin :
    #     arrMin=arr[i]
for x in arr:
    if x<arrMin:
        arrMin=x


print(arrMin)