def lower_bound(arr,n,k):
  l=0
  r=n
  while l<r:
    mid=(l+r)//2
    if arr[mid]<k:
      l=mid+1
    else:
      r=mid
  if l<n and arr[l]==k:
    return l
  else:
    return -1
  

def upper_bound(arr,n,k):
  l=0
  r=n
  while l<r:
    mid=(l+r)//2
    if arr[mid]<=k:
      l=mid+1
    else:
      r=mid
  if l>0 and arr[l-1]==k:
    return l-1
  else:
    return -1    
  


def upper_lower_bound(arr,n,k):
  l_bound=lower_bound(arr,n,k)
  u_bound=upper_bound(arr,n,k)  
  if l_bound== -1:
    return -1, -1, 0
  count=u_bound - l_bound +1
  return  l_bound , u_bound, count


n=int(input())
arr=list(map(int,input().split()))
k=int(input())
ans=upper_lower_bound(arr,n,k)
print(*ans)