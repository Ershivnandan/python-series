
# def spiralDiagonalsSum(t, cases):
#   for case in cases:
#     N, spiral = case
#     matrix = [[0] * N for _ in range(N)]
#     top, bottom, left, right = 0, N - 1, 0, N - 1
#     idx = 0

#     while top <= bottom and left <= right:
#       for i in range(left, right + 1):
#         matrix[top][i] = spiral[idx]
#         idx += 1
#       top += 1

#       for i in range(top, bottom + 1):
#         matrix[i][right] = spiral[idx]
#         idx += 1
#       right -= 1

#       if top <= bottom:
#         for i in range(right, left - 1, -1):
#           matrix[bottom][i] = spiral[idx]
#           idx += 1
#         bottom -= 1

#       if left <= right:
#         for i in range(bottom, top - 1, -1):
#           matrix[i][left] = spiral[idx]
#           idx += 1
#         left += 1

#     diagonal_sum = sum(matrix[i][i] for i in range(N)) + sum(matrix[i][N - 1 - i] for i in range(N))
#     if N % 2 == 1:
#       diagonal_sum -= matrix[N // 2][N // 2]
#     print(diagonal_sum)

# t = int(input())
# cases = []

# for _ in range(t):
#   N = int(input())
#   spiral = list(map(int, input().split()))
#   cases.append((N, spiral))

# spiralDiagonalsSum(t, cases)


# def weightLifting(arr, n):
  
#   h = 0 
#   j = n-1
#   Harry = 0
#   john = 0
#   flag = True
#   temp = 0
#   prev = 0
  
#   while h < j:
#     if flag:
#       if temp + arr[h] > prev:
#         prev = temp + arr[h]
#         Harry += temp + arr[h]
#         h += 1
#         flag = False
#         temp = 0
#       elif temp < prev:
#         temp += arr[h]
#         h +=1
#     else:
#       if temp + arr[j] > prev:
#         prev = arr[j] + temp
#         john += temp + arr[j]
#         j -=1
#         flag = True
#         temp = 0
#       elif temp < prev:
#         temp += arr[j]
#         j -=1
  
#   print(Harry, john)



# n = 11
# arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# weightLifting(arr, n)


def functionC(s, N):
    head = 0
    dictionary = {}
    res = 0

    for tail in range(N):
        key = s[tail]

        while key in dictionary and dictionary[key] > 0:
            res= max(res, tail - head)
            dictionary[s[head]] -= 1
            head += 1
            
        if key in dictionary:
            dictionary[key] +=1
        else:
            dictionary[key] = 1
            
    print(res)
        


arr = ["a", "b", "b", "c", "d", "e", "a", "b", "b"]

functionC(arr, len(arr))