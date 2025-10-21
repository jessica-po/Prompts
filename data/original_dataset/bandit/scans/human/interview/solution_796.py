fa = [1]
m = 251
P = 10**9+7
for i in range(1, m+1): fa.append(fa[-1] * i % P)
fainv = [pow(fa[m], P-2, P)]
for i in range(1, m+1)[::-1]: fainv.append(fainv[-1] * i % P)
fainv = fainv[::-1]
def C(a, b): return fa[a] * fainv[a-b] * fainv[b] % P

N, K = list(map(int, input().split()))
poK = [1]
for i in range(251): poK.append(poK[-1] * K % P)
poK1 = [1]
for i in range(251): poK1.append(poK1[-1] * (K-1) % P)

dpC = [[C(i, j) for j in range(i+1)] for i in range(N+1)]
dpCpoK = [[C(i, j) * poK[j] % P for j in range(i+1)] for i in range(N+1)]

DP = [[0] * (N+1) for _ in range(N+1)]
DP[0][0] = 1
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(j+1):
            if k < j:
                DP[i][j] = (DP[i][j] + DP[i-1][k] * dpCpoK[j][k]) % P
            else:
                DP[i][j] = (DP[i][j] + DP[i-1][k] * dpC[j][k] % P * (poK[k] - poK1[k])) % P
    for j in range(1, N+1):
        DP[i][j] = DP[i][j] * poK1[N-j] % P

print(DP[N][N])