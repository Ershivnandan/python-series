def findSum(arr, n, k):

    for i in range(n):
        count_subarr = 0
        temp = []
        for j in range(i, n):
            count_subarr += arr[j]
            temp.append(arr[j])
            if count_subarr == k:
                print(temp)
                print(True)
                return
    print(False)


arr = [1, 4, 3, 2, 5, 7]
  #    0  1  2  3  4  5
k = 10

n = len(arr)

findSum(arr, n ,k)