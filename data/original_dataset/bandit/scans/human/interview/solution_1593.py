n, s = map(int, input().split())
c = []
for i in range(n):
    x, y, z = map(int, input().split())
    c.append((x, y, z))
minans = 10**20
for i in range(n):
    nc = 0
    total = s
    for j in range(n):
        if c[j][0] ** 2 + c[j][1] ** 2 <= c[i][0] ** 2 + c[i][1] ** 2:
            total += c[j][2]
    if total >= 10**6 and c[i][0] ** 2 + c[i][1] ** 2 < minans:
        minans = c[i][0] ** 2 + c[i][1] ** 2
if minans != 10**20:
    print(minans ** 0.5)
else:
    print(-1)