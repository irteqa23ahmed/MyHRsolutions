# Longest common subsequence size (Recursion)
def lcs(x,y,m,n):
  if (m==0 or n==0):
    return 0
  elif (x[m-1] == y[n-1]):
    return 1+lcs(x,y,m-1,n-1)
  else:
    return max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))

x = "abcdef"
y = "awebghd"

print(lcs(x,y,len(x),len(y)))

###################################################################################################

# Longest common substring size
def lcs(x,y,m,n):
  t = [[0 for _ in range(n+1)] for j in range(m+1)]
  max_val = 0
  for i in range(1,m+1):
    for j in range(1,n+1):
      if x[i-1] == y[j-1]:
        t[i][j] = 1 + t[i-1][j-1]
        max_val = max(t[i][j],max_val)
      else:
        t[i][j] = 0
  return max_val

x = "abcdef"
y = "eacdghd"

print(lcs(x,y,len(x),len(y)))
