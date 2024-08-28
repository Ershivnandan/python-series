def solve(arr):
    N = len(arr)
    mid = N // 2
    result = []


    for i in range(N):
        start_col = abs(mid - i)
        end_col = N - start_col
        for j in range(start_col, end_col):
            result.append(arr[i][j])
    

    for val in result:
        print(val, end=" ")


arr = [
 [ 43 , 64,  96,  32, 100,  19,   9],
 [ 68 , 23,  33,  68,  86,  40,  99],
 [ 50 , 87,  14,   4,  17,  96,  59],
 [  2 ,  9,  26,  50,   3,  88,  10],
 [  4 , 54,  80,  66,  41,  72,   6],
 [ 52 , 65,  62,  28,  65,  36,  87],
 [ 12 , 15,  57,  28,  76,   9,  42]
]

solve(arr)