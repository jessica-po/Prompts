read = lambda: map(int, input().split())
n = int(input())
s = input()
a = list(read())
dp = [0] * (n + 2)
mn = [10 ** 4] * (n + 2)
dp[0] = dp[n + 1] = 1
mn[n + 1] = 0
mn[0] = 1
Max = 1
mod = 10 ** 9 + 7
for i in range(1, n):
    res = 0
    cur = 10 ** 4
    for j in range(i, -1, -1):
        c = ord(s[j]) - ord('a')
        cur = min(cur, a[c])
        if cur < (i - j + 1):
            break
        dp[i] = (dp[i] + dp[j - 1]) % mod
        mn[i] = min(mn[i], mn[j - 1] + 1)
        Max = max(Max, i - j + 1)
print(dp[n - 1])
print(Max)
print(mn[n - 1])