def solve(matrix):
    N = len(matrix)

    for i in range(N):
        if i < N-2:
            print(matrix[i][0], end= ' ')
            print(matrix[i][1], end=' ')
        elif i < N-1:
            print(matrix[i][0], end=' ')
        
    for i in range(N):
        print(matrix[(N-1)-i][i], end=' ')
    
    for i in range(1, N):
        if i == 1:
            print(matrix[i][N-1], end=' ')
        else:
            print(matrix[i][N-2], end=' ')
            print(matrix[i][N-1], end=' ')



matrix = [
    [10, 19, 41, 22, 32, 15, 5, 12, 13],
    [10, 19, 41, 22, 32, 15, 5, 12, 13],
    [10, 19, 41, 22, 32, 15, 5, 12, 13],
    [10, 19, 41, 22, 32, 15, 5, 12, 13],
    [10, 19, 41, 22, 32, 15, 5, 12, 13],
    [10, 19, 41, 22, 32, 15, 5, 12, 13],
    [10, 19, 41, 22, 32, 15, 5, 12, 13],
    [10, 19, 41, 22, 32, 15, 5, 12, 13],
    [10, 19, 41, 22, 32, 15, 5, 12, 13],
]

solve(matrix)
