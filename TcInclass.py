def solve(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                print(True)
                return
    print(False) 

arr = [1, 2, 3, 4, 5]

# a and b 
k = 10

solve(arr, k)
    

