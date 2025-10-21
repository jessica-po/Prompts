# dp[i] := i 項目以降を見たときの場合の数
#       = dp[i+1] + (Σ_{3<=d<=N-1} dp[i+d]) + (n-1)**2

# i 項目と i+1 項目について、
#   (1) i 項目が 1 の場合
#   (2) i 項目が 1 で無く、i+1 項目が 1 の場合
#   (3) i 項目も i+1 項目も 1 で無い場合
# で場合分けしてそれぞれを足している
# これを累積和で高速化する

# 初期化がややこしい

N = int(input())
mod = 10**9+7
dp = [N] * (N+1)
dp[N-1] = N
dp[N-2] = N*N
c = N * (N+1) + N-1
const = (N-1)**2
for i in range(N-3, -1, -1):
    ans = c - dp[i+2] + const
    dp[i] = ans
    c = (c + ans - 1) % mod
print((dp[0]%mod))