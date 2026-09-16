arr = [13, 40, 24, 52, 20, 9]
for i in range(len(arr)-1):
    min_index = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
print(arr)