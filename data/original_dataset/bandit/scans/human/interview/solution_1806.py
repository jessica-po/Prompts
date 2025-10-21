import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
A = []
for _ in range(N):
    l, r = list(map(int, input().split()))
    A.append([l, r])
Z = []
for _ in range(M):
    l, r = list(map(int, input().split()))
    Z.append([l, r])
MA = 5*10**5+1
lg = 20

X = [[-1]*MA for i in range(lg)]
for i in range(N):
    X[0][A[i][0]] = max(X[0][A[i][0]], A[i][1])
for i in range(1, MA):
    X[0][i] = max(X[0][i], X[0][i-1])

for k in range(1, lg):
    for i in range(MA):
        a = X[k-1][i]
        if a >= 0:
            X[k][i] = X[k-1][a]

for a, b in Z:
    ans = 1
    for k in range(lg)[::-1]:
        if X[k][a] < b:
            a = X[k][a]
            ans += 2**k
    print(-1 if X[0][a] < b or ans > MA else ans)