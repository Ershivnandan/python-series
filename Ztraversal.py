def solve(A):
    N = len(A)
    result = []

    for j in range(N):
        result.append(A[0][j])
    
    for i in range(1, N-1):
        result.append(A[i][N-i-1])
    
    for j in range(N):
        result.append(A[N-1][j])
    
    for val in result:
        print(val, end=" ")


N = int(input("Enter the size of the matrix: "))
A = []
print("Enter the matrix row by row:")
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

solve(A)
