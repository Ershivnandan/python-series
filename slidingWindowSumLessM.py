def arrLessM(arr, n, m):

    start = 0
    count = 0
    sum = 0

    for end in range(n):

        sum += arr[end]
        if sum < m:
            count +=1
            
        while sum >= m:
            sum -= arr[start]
            start +=1
        
        
    print(count)

arr = [1, 5, 1, 3, 2]

arrLessM(arr, 5, 5)