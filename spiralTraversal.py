
def solve(arr, n):
    top =0 
    left = 0
    bottom = n-1
    right = n-1

    while(top <= bottom and left <=right):

        for j in range(left, right+1, 1):
            print(arr[top][j])

        top += 1

        for i in range(top, bottom+1, 1):
            print(arr[i][right])

        right -= 1

        for j in range(right, left, -1):
            print(arr[bottom][j])
        
        bottom -= 1

        for i in range(bottom, top, -1):
            print(arr[i][left])
        
        left += 1





arr = [
 [ 43 , 64,  96,  32, 100,  19,   9],
 [ 68 , 23,  33,  68,  86,  40,  99],
 [ 50 , 87,  14,   4,  17,  96,  59],
 [  2 ,  9,  26,  50,   3,  88,  10],
 [  4 , 54,  80,  66,  41,  72,   6],
 [ 52 , 65,  62,  28,  65,  36,  87],
 [ 12 , 15,  57,  28,  76,   9,  42]
 ]

n = len(arr)

solve(arr, n)