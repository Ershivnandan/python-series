def NearestSmallerOnLeft(arr, n):

    stack = []
    res = [-1] * n
    stack.append(0)

    for i in range(1, n):

        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        if stack:
            res[i] = arr[stack[-1]]

        stack.append(i)
    
    print(*res)


# def NearestGreaterOnLeft(arr, n):

#     stack = []
#     res = [-1] * n
#     stack.append(0)

#     for i in range(1, n):

#         while stack and arr[stack[-1]] <= arr[i]:
#             stack.pop()
        
#         if stack:
#             res[i] = arr[stack[-1]]

#         stack.append(i)
    
#     print(*res)
            


arr = [7,2,4,6,9,3,8,11]
n = len(arr)
NearestSmallerOnLeft(arr, n)