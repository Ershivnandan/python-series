def solution(arr, n, k):

    sumn = 0
    for i in range(k):
        sumn += arr[i]
    res=sumn
    for i in range(k, n):
        sumn = sumn-arr[i-k]+arr[i]
        res = max(res,sumn)

    print(res)

array=[1,2,3,4,5,6,7,8,9]
n=len(array)
solution(array, n, 4)

