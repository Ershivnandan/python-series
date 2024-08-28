def nextSmallerOfNextGreater(arr, n):

  
  nge = [-1] * n
  stack = []
  
  for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
      nge[stack.pop()] = i
    stack.append(i)
  
  result = [-1] * n
  
  for i in range(n):
    if nge[i] != -1:
      j = nge[i]
      for k in range(j + 1, n):
        if arr[k] < arr[j]:
          result[i] = arr[k]
          break
  
  return result

# t = int(input())

# for _ in range(t):
#   n = int(input())
#   arr = list(map(int, input().split()))

n = 6
arr = [5, 1, 6, 2, 5, 1]

result = nextSmallerOfNextGreater(arr, n)
print(" ".join(map(str, result)))
