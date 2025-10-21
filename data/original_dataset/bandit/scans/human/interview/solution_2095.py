n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
res = []
for i in range(n):
    j = 0
    while j < n and 3 != a[i][j] != 1:
        j += 1
    if j == n: res.append(i + 1)
print(len(res))
print(' '.join(map(str, res)))