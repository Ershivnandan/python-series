def power_sum(x,n,c):
  if x==0:
    return 1
  if x<0 or c**n>x:
    return 0
  inc=power_sum(x-c**n, n, c+1)
  exc=power_sum(x, n, c+1)
  return inc+exc
  

x,n=map(int,input().split())
ans=power_sum(x,n,1)
print(ans)