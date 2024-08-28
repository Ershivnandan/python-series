def hassanSortingAlgo(arr, n, k):
  
  for i in range(n):
    
    for j in range(0, n-i-1):
      
      if ((arr[j])%k) > ((arr[j+1])%k):
        temp = arr[j+1]
        arr[j+1] = arr[j]
        arr[j] = temp
        
      elif arr[j]%k == arr[j+1]%k:
        continue
      
  print(*arr)

N, K = map(int, input().split())

arr = list(map(int, input().split()))

hassanSortingAlgo(arr, N, K)