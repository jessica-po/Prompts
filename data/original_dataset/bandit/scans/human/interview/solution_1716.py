N, M, Q = list(map(int, input().split()))

table = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    L, R = list(map(int, input().split()))
    table[L][R] += 1

for i in range(N+1):
    for j in range(N):
        table[i][j+1] += table[i][j]
for i in range(N):
    for j in range(N+1):
        table[i+1][j] += table[i][j]

for _ in range(Q):
    p, q = list(map(int, input().split()))
    print((table[q][q] - table[q][p-1] - table[p-1][q] + table[p-1][p-1]))