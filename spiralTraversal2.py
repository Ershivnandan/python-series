def spiralPrint(A):
    if not A:
        return
    
    top = 0
    bottom = len(A) - 1
    left = 0
    right = len(A[0]) - 1
    print(right)
    
    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            print(A[top][i], end=' ')
        top += 1
        
        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            print(A[i][right], end=' ')
        right -= 1
        
        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                print(A[bottom][i], end=' ')
            bottom -= 1
        
        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                print(A[i][left], end=' ')
            left += 1

A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

spiralPrint(A)
