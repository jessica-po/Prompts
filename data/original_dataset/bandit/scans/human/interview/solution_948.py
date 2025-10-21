n, m = list(map(int, input().split()))

field = []
for i in range(n):
    field.append(input())

ans = 0
for i in range(n - 1):
    for j in range(m - 1):
        t = set()
        t.add(field[i][j])
        t.add(field[i + 1][j + 1])
        t.add(field[i + 1][j])
        t.add(field[i][j + 1])

        if t == set('face'):
            ans += 1
print(ans)