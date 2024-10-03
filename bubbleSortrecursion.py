def recursive_sort(array,n):
  if n==1:
    return array
  
  for i in range(n-1):
    if array[i]>array[i+1]:
      array[i],array[i+1]=array[i+1],array[i]
      
  return recursive_sort(array,n-1)    


n=int(input())
array=list(map(int,input().split()))
ans=recursive_sort(array,n)
print(*ans)