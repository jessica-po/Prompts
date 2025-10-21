N = int(input())
X = [i for i in range(N+1)]
Y = [[] for _ in range(N)]
B, W = [], []
ans = 0
for i in range(2 * N):
    c, a = input().split()
    a = int(a) - 1
    if c == "B":
        X = [X[i] + 1 if i <= a else X[i] - 1 for i in range(N+1)]
        B.append(a)
        ans += len([b for b in B if b > a])
    else:
        Y[a] = X[:]
        W.append(a)
        ans += len([b for b in W if b > a])

Z = [0] * (N+1)
for y in Y:
    for i in range(N+1):
        Z[i] += y[i]
    for i in range(1, N+1):
        Z[i] = min(Z[i], Z[i-1])

ans += Z[-1]
print(ans)