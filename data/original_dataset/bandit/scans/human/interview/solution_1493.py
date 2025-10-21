n, m = map(int, input().split())

fin = [list(input().strip()) for i in range(n)]
ans = [['-' for i in range(m)] for j in range(n)]

for y in range(n):
    for x in range(m):
        if fin[y][x] == '-':
            continue
        elif y % 2 == x % 2:
            ans[y][x] = 'B'
        else:
            ans[y][x] = 'W'
for row in ans:
    print(''.join(row))