n = int(input())
dp = [0] * (n + 1)
maxlev = 0
mod = 1000000007
lst = "s"
dp[0] = 1
for i in range(n):
  s = input()
  if lst == "f":
    for j in reversed(range(1, maxlev+2)):
      dp[j] = dp[j-1]
    maxlev += 1
    dp[0] = 0
  else:
    sum = 0
    for j in reversed(range(0, maxlev+1)):
      sum = (sum + dp[j]) % mod
      dp[j] = sum
  lst = s
res = 0
for i in range(0, maxlev + 1):
  res = (res + dp[i]) % mod
print(res)