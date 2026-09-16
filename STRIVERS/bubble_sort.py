arr = [13, 40, 24, 52, 20, 9]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        did_swap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                did_swap = True
        if did_swap == False:
            break   
bubble_sort(arr)
print(arr)