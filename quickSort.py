def partition(arr, l, r):
    pivot = arr[r]

    i = l - 1

    for j in range(l, r):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1

def quickSort(arr, l, r):
    if l < r:

        p = partition(arr, l, r)

        quickSort(arr, l, p-1)
        quickSort(arr, p+1, r)

arr = [8, 7, 2, 1, 0 ,9, 6]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)