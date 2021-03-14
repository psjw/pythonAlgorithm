array=[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

#selection sort
for i in range(len(array)):    
    tempIdx=i
    for j in range(i+1,len(array)): 
        if array[tempIdx] > array[j] :
            tempIdx=j
    array[i],array[tempIdx] = array[tempIdx],array[i]

print(array)