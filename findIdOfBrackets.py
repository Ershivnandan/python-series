

def assignId(s,n):

    st = []
    res = []
    for i in range(n):

        if st and s[st[-1]-1] == "(" and s[i] == ")":
            res.append(st.pop())
        else:
            st.append(i+1)
            res.append(i+1)

    print(*res)


s = "))(())"

n = len(s)

assignId(s,n)