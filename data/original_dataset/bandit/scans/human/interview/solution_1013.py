n, m = list(map(int, input().split()))
A = [input().split() for i in range(n)]
T = False
for i in range(n):
    for j in range(m):
        if A[i][j] == '1' and (i == 0 or j == 0 or i == n - 1 or j == m - 1):
            T = True
if T:
    print(2)
else:
    print(4)