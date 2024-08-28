st = "([{)}]"

def isBalanced(st):

    n= len(st)
    stack = []
    if n %2 ==1:
        return False
    
    for i in range(n):
        ch = st[i]

        if ch == "{" or ch == "(" or ch == "[":
            stack.append(ch)
        else:
            ch2 = stack.pop()

            if ch2 == '{' and ch != "}" or ch2 == '(' and ch != ")" or ch2 == '[' and ch != "]":
                return False
    
    return True


res = isBalanced(st)

print(res)

