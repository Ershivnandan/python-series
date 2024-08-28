def checkVailaid(string, n):
  stack = []
  
  if n % 2 != 0:
    print("not balanced")
    return
  elif string[0] == ")" or string[0] == "}" or string[0] == "]":
    print("not balanced")
    return
  
  for i in range(n):
    ch = string[i]
    
    if ch == "{" or ch == "(" or ch == "[":
      stack.append(ch)
    elif ch == "}" or ch == ")" or ch == "]":
      if not stack:
        print("not balanced")
        return
      else:
        ch2 = stack.pop()
        
        if ch == ")" and ch2 != "(" or ch == "]" and ch2 != "[" or ch == "}" and ch2 != "{":
          print("not balanced")
          return
        
  if not stack:
    print("balanced")
  else:
    print("not balanced")

string = "[one[two[three[four[five[six[seven[eight[nine[ten]]]]]]]]]]"

n = len(string)

checkVailaid(string, n)