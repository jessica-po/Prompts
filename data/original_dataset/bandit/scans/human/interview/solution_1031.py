n = int(input())
a = [int(i) for i in input().split()]
miny = 0
maxy = 0
s = 0
for i in range(n):
    if i % 2 == 0:
        s += a[i]
    else:
        s -= a[i]
    maxy = max(s, maxy)
    miny = min(s, miny)
dif = maxy - miny
size = sum(a)
res = [[" "] * size for i in range(dif)]
cur = [maxy, 0]
for i in range(n):
    if i % 2 == 0:
        cur[0] -= 1
    else:
        cur[0] += 1
    for j in range(a[i]):
        if i % 2 == 0:
            res[cur[0]][cur[1]] = "/"
            cur[0] -= 1
        else:
            res[cur[0]][cur[1]] = "\\"
            cur[0] += 1
        cur[1] += 1

for i in res:
    print("".join(i))