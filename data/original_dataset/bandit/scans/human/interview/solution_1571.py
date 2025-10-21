S = input()
T = input()
base = 998244353
dp = [[0 for _ in range(len(S) + 1)] for _ in range(len(S) + 1)]
for j in range(1, len(S) + 1):
    if (j > len(T)) or (S[0] == T[j - 1]):
        dp[1][j] = 2
for i in range(2, len(S) + 1):
    for j in range(1, len(S) - i + 1 + 1):
        if (j > len(T)) or (S[i - 1] == T[j - 1]):
            dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % base
        if (j + i - 1 > len(T)) or (S[i - 1] == T[j + i - 1 - 1]):
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % base
ans = 0
for i in range(len(T), len(S) + 1):
    ans = (ans + dp[i][1]) % base
print(ans)