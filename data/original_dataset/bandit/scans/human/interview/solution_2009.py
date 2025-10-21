n = int(input())
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
a = [['1'] * (n + 2)]
for _ in range(n):
    s = input()
    d = ['1']
    for i in s:
        d.append(i)
    d.append('1')
    a.append(d)
a.append(['1'] * (n + 2))
s = []
f = []
q = [[r1, c1]]
while q:
    x, y = q.pop()
    a[x][y] = '1'
    s.append([x, y])
    if a[x - 1][y] == '0':
        q.append([x - 1, y])
    if a[x][y - 1] == '0':
        q.append([x, y - 1])
    if a[x + 1][y] == '0':
        q.append([x + 1, y])
    if a[x][y + 1] == '0':
        q.append([x, y + 1])
if [r2, c2] in s:
    print(0)
else:
    q = [[r2, c2]]
    while q:
        x, y = q.pop()
        a[x][y] = '1'
        f.append([x, y])
        if a[x - 1][y] == '0':
            q.append([x - 1, y])
        if a[x][y - 1] == '0':
            q.append([x, y - 1])
        if a[x + 1][y] == '0':
            q.append([x + 1, y])
        if a[x][y + 1] == '0':
            q.append([x, y + 1])
    res = 10**10
    for i in s:
        for j in f:
            res = min(res, (i[0] - j[0])**2 + (i[1] - j[1])**2)
    print(res)