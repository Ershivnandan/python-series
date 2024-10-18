def generateAllSubSequences(strn, ans, i, n):
  
  if i == n:
    return 
  ans.append(strn[i])
  print("".join(ans))
  
  generateAllSubSequences(strn, ans, i+1, n)
  
  ans.pop()
  
  generateAllSubSequences(strn, ans, i+1, n)
  
n = int(input())

if n <= 18:
  strn = input()
  ans = []
  generateAllSubSequences(strn, ans, 0, n)

