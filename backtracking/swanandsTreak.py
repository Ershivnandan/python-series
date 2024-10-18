def track(n, matrix, px, py, prev, path):
  if px < 0 or py < 0 or px >= n or py >= n or matrix[px][py] <= prev:
    return ""
  
  path += str(matrix[px][py]) + " "
  
  next_position = check_path(n, matrix, px, py, matrix[px][py])
  if next_position[0] == px and next_position[1] == py:
    return path
  
  return track(n, matrix, next_position[0], next_position[1], matrix[px][py], path)

def check_path(n, matrix, px, py, prev):
  current_position = (px, py)
  min_value = float('inf')

  if px - 1 >= 0 and matrix[px - 1][py] > prev:
    current_position = (px - 1, py)
    min_value = matrix[px - 1][py]
  if px + 1 < n and matrix[px + 1][py] > prev and matrix[px + 1][py] < min_value:
    current_position = (px + 1, py)
    min_value = matrix[px + 1][py]
  if py + 1 < n and matrix[px][py + 1] > prev and matrix[px][py + 1] < min_value:
    current_position = (px, py + 1)
    min_value = matrix[px][py + 1]
  if py - 1 >= 0 and matrix[px][py - 1] > prev and matrix[px][py - 1] < min_value:
    current_position = (px, py - 1)
    min_value = matrix[px][py - 1]

  return current_position

n = int(input())

px, py = map(int, input().split())
matrix = []
for i in range(n):
  arr = list(map(int, input().split()))
  matrix.append(arr)

output = []
output.append(track(n, matrix, px - 1, py, matrix[px][py], str(matrix[px][py]) + " "))
output.append(track(n, matrix, px + 1, py, matrix[px][py], str(matrix[px][py]) + " "))
output.append(track(n, matrix, px, py + 1, matrix[px][py], str(matrix[px][py]) + " "))
output.append(track(n, matrix, px, py - 1, matrix[px][py], str(matrix[px][py]) + " "))

for path in output:
  if path:
    print(path.strip())
  else:
    print(-1)
