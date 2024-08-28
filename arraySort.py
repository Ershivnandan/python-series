
def sortArr(arr):
    n = len(arr)
    newArr= []
    for i in range(n-1, 0, -1):
        
        swaped = False

        for j in range(i):
            if arr[j] > arr[j+1]:
                swaped = True
                newArr.append(j-i)
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                newArr.append(j)

        if not swaped:
            break
    return newArr

arr = [1,4,3,2,5]

res = sortArr(arr)

print(arr)
print(res)
        