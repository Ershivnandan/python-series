def lower_bound(arr,n,k):
  l=0
  r=n
  while l<r:
    mid=(l+r)//2
    if arr[mid]>=k:
      r=mid
    else:
      l=mid+1
  if arr[l]==k and l<n:
    return l
  else:
    return -1



n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans=lower_bound(arr,n,k)
print(ans)