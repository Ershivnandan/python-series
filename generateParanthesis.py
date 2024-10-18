def generateParanthesis(n, openC=0, closeC=0, curr="", res=[]):
  
  if len(curr) == 2*n:
    res.append(curr)
    return
  
  
  if openC < n:
    generateParanthesis(n, openC + 1, closeC, curr+"(", res)
  
  if closeC < openC:
    generateParanthesis(n, openC, closeC + 1, curr+")", res)
    

def vailaidParanthesis(n):
  
  res = []
  
  generateParanthesis(n,0, 0, "", res)
  
  res.sort()
  
  print(len(res))
  for para in res:
    print(para)

t = int(input())

for i in range(t):
  
  n = int(input())
  
  vailaidParanthesis(n)
  


# Nick and hacks 

#   def nickAndHacks(n, nick=1):
  
#   if nick == n:
#     return "Yes"
#   if nick > n:
#     return "No"
  
#   res1 = nickAndHacks(n, nick * 10)
#   res2 = nickAndHacks(n, nick * 20)
  
#   return "Yes" if res1 == "Yes" or res2 == "Yes" else "No"

# t = int(input())

# for i in range(t):
#   n = int(input())
  
#   res = nickAndHacks(n)
  
#   print(res)



# Knight Chess 


# def playChess(i, j, n, mat):
  
#   if i < 0 or i >= 10 or j < 0 or j >= 10:
#     return
#   if n == 0:
#     mat[i][j] = 1
#     return
  
#   playChess(i-2, j+1, n-1, mat)
#   playChess(i-1, j+2, n-1, mat)
#   playChess(i+1, j+2, n-1, mat)
#   playChess(i+2, j+1, n-1, mat)
#   playChess(i+2, j-1, n-1, mat)
#   playChess(i+1, j-2, n-1, mat)
#   playChess(i-1, j-2, n-1, mat)
#   playChess(i-2, j-1, n-1, mat)
  

# i, j, N = map(int, input().split())

# if N < 10:
  
#   mat = [[0 for _ in range(10)] for _ in range(10)]
#   # print(mat)
#   playChess(i-1, j-1, N, mat)
#   count = 0
  
#   for arr in mat:
#     for i in arr:
#       if i == 1:
#         count += 1
  
#   print(count)
  
  
  