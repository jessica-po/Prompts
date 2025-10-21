import numpy as np
 
N, T = map(int, input().split())
data = []
for i in range(N):
  a, b = map(int, input().split())
  data.append((a,b))
data.sort()
data = np.array(data)

dp = np.zeros(T)
ans = 0
for a, b in data:
    ans = max(ans,dp[-1]+b)
    if a< T:
        newtable = dp[:T-a] + b
        dp[a:] = np.maximum(dp[a:], newtable)

print(int(ans))