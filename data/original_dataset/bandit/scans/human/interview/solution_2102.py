from sys import stdin
input = stdin.readline

a = sorted([int(i) for i in input().split()])
n = int(input())
b = sorted([int(i) for i in input().split()])

c = []
for i in range(n):
    c += [[b[i] - a[j], i] for j in range(6)]
c.sort()

d = [0] * n
e = 0

ans = 10 ** 10

u = 0
for i in range(len(c)):
    while u < len(c) and e < n:
        x = c[u][1]
        if d[x] == 0:
            e += 1
        d[x] += 1
        u += 1

    if e == n:
        ans = min(ans, c[u - 1][0] - c[i][0])

    x = c[i][1]
    d[x] -= 1
    if d[x] == 0:
        e -= 1

print(ans)