n,m=map(int,input().split())
arr=list(map(int,input().split()))
high=max(arr)

def  wood_cutter(arr,m,n,high):
  low=1
  while low<=high:
    mid=low+(high-low)//2
    temp=mid_value(arr,m,n,mid)
    if temp==0:
      return mid
    if temp>0:
      high=mid-1
    else:
      low=mid+1
  return -1

def mid_value(arr,m,n,mid):
  res=m
  for i in range(n):
    if mid<arr[i]:
      res-=arr[i]-mid
  return res
  
  
print(wood_cutter(arr,m,n,high))