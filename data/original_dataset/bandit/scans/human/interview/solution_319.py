n, m = list(map(int, input().split()))
a = [list(map(int, input())) for i in range(n)]

ignorable = [True] * n

for i in range(m):
    cnt = 0
    for j in range(n):
        cnt += a[j][i]
    if cnt == 1:
        for j in range(n):
            if a[j][i]:
                ignorable[j] = False

if any(ignorable):
    print('YES')
else:
    print('NO')