def flowerbed(arr, n):
    # res= [0] * n
    for i in range(n):

        if i == 0 and arr[i+1] == 0 or i == n-1 and arr[i-1] == 0:
            arr[i] = 1
        elif arr[i] == 0 and arr[i-1] == 0 and arr[i+1] == 0:
            arr[i] = 1
        else:
            continue
    
    # flag = True
    # for i in range(n):



arr = [0,0,1,0,1,0,0,0,1]

n = len(arr)

flowerbed(arr, n)