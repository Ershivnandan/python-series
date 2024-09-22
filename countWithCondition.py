def countX(arr, s, e, x, subset):
  if s > e:
    if sum(subset) == x:
      return 1
    return 0
  
  count = 0
  count += countX(arr, s + 1, e, x, subset + [arr[s]])
  count += countX(arr, s + 1, e, x, subset)
  
  return count

def countWithCondition(arr, n, x):
  return countX(arr, 0, n - 1, x, [])

n, x = 4, 10                                                                                                        
arr = [1, 2, 3, 4]

res = countWithCondition(arr, n, x)
print(res)
