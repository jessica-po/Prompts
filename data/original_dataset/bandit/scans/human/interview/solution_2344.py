n = int(input())
a = [tuple(map(int, input().split())) for i in range(n)]

a = [(y, x, k) for x, y, k in a]
a.sort(reverse=True)
dp = [[-1] * (n + 1) for i in range(n)]

def f(i, j):
    if i < 0 or j < -1: return 0
    if dp[i][j] == -1:
        y, x, k = a[i]
        dp[i][j] = f(i - 1, j) + max(0, x - k * y)
        if 0 <= j < k: dp[i][j] = max(dp[i][j], x - j * y + f(i - 1, j - 1))
    return dp[i][j]

print(max(f(n - 1, j) for j in range(-1, n)))