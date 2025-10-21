n, k = map(int, input().split())
ans = [[0 for i in range(n)]for j in range(n)]
cur = 1
sum_k = 0
for i in range(n):
    for j in range(k-1):
        ans[i][j] = cur
        cur += 1
for i in range(n):
    for j in range(k-1, n):
        ans[i][j] = cur
        cur += 1
for i in range(n):
    sum_k += ans[i][k-1]
print(sum_k)
for i in range(n):
    for j in range(n):
        print(ans[i][j], end = ' ')
    print('')