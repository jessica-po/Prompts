from collections import defaultdict as dd

def find(a, b):
 n = len(a)
 m = len(b)

 dp = [[0]*(m+1) for i in range(n+1)]

 for i in range(n-1,-1, -1):
  for j in range(m-1, -1, -1):
   if a[i] == b[j]:
    dp[i][j] = dp[i+1][j+1] + 1

 mx = dd(int)
 ans = 0
 for i in range(n-1, -1, -1):
  for j in range(m-1, -1, -1):
   a = mx[(i+1, j)]
   b = mx[(i, j+1)]
   mx[(i, j)] = max([dp[i][j], a, b])

 for i in range(n):
  for j in range(m):
   c = dp[i][j]
   nxt = mx[(i+c, j+c)]
   cur = c + nxt
   ans = max(ans, cur)
   
 return 2*ans
for case in range(int(input())):
 a, b = input().split()
 b = b[-1::-1]

 ans = find(a, b)
 print(ans)