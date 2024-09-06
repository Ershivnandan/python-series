def flowerbed(arr, n,m):
    # res= [0] * n
    for i in range(n):
        if m <= 0:
            break
        elif i == 0 and arr[i+1] == 0 or i == n-1 and arr[i-1] == 0:
            arr[i] = 1
            m -= 1
        elif arr[i] == 0 and arr[i-1] == 0 and arr[i+1] == 0:
            arr[i] = 1
            m -= 1
        else:
            continue
    
    # flag = True
    # for i in range(n):
    # print(*arr)
    if m <= 0:
        print(True)
    else:
        print(False)



arr = [0,0,1,1,1,0,0,0,1]

n = len(arr)

flowerbed(arr, n, 1)