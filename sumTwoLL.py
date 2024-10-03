def addTwoNumbers(A, B):
  x=A
  y=B
  carry=0
  temp=Node(0)
  curr=temp
  while x or y:
    total=carry
    if x:
      total+=x.data
      x=x.next
    if y:
      total+=y.data
      y=y.next
    
    carry = total//10
    curr.next = Node(total%10)
    curr = curr.next
  return temp.next