tc = int(input())

for _ in range(tc):
  n = int(input())
  arr = list(map(int, input().split()))
  left=[-1]*n
  right=[-1]*n
  stack=[]

  for i in range(n):
    while stack and arr[stack[-1]]<=arr[i]:
      stack.pop()
    if stack:
      left[i]=stack[-1]
    stack.append(i)

  stack=[]

  for i in range(n-1,-1,-1):
    while stack and arr[stack[-1]]<=arr[i]:
      stack.pop()
    if stack:
      right[i]=stack[-1]
    stack.append(i)

  for i in range(n):
    left_distance = abs(i - left[i]) if left[i] != -1 else float('inf')
    right_distance = abs(i - right[i]) if right[i] != -1 else float('inf')
        
    if left_distance == float('inf') and right_distance == float('inf'):
      print(-1,end=" ")
    elif left_distance <= right_distance:
      print(arr[left[i]],end=" ")
    else:
      print(arr[right[i]],end=" ")
      
  print()