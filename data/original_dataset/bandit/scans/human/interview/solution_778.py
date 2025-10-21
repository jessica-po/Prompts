def check(l, r, a, b):
    if a < 0 or b >= 2 * N:
        return 0
    def val(p):
        if p in [a, b]: return '0'
        if l <= p and p < r: return '1'
        return '-1'
    for i in range(K):
        x, y = val(A[i]), val(C[i])
        if A[i] in [a, b] or C[i] in [a, b]:
            if not eval(x + B[i] + y):
                return 0
    return 1

N, K = list(map(int, input().split()))
tmp = [input().split() for i in range(K)]
try: A, B, C = list(zip(*tmp))
except: A, B, C = [], [], []
A = [int(x) - 1 for x in A]
B = ['==' if x is '=' else x for x in B]
C = [int(x) - 1 for x in C]

dp = []
for i in range(N + 1):
    dp.append([0] * (2 * N + 1))

dp[N][0] = 1
for i in range(N, 0, -1):
    for j in range(0, 2 * (N - i) + 3):
        d, k = 0, j + 2 * i - 2
        if check(j, k, j - 2, j - 1): d += dp[i][j - 2]
        if check(j, k, j - 1, k): d += dp[i][j - 1]
        if check(j, k, k, k + 1): d += dp[i][j]
        dp[i - 1][j] = d

print(sum(dp[0]) // 3)