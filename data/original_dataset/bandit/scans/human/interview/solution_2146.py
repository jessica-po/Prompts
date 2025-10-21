n = int(input())
a = list([int(x) - 1 for x in input().split()])

cnt = 0
curr = [0]
v = [0 for _ in range(n)]
r = [0 for _ in range(n)]

lvl = 0
while cnt < n:
    nxt = []
    for i in curr:
        if v[i]:
            continue
        v[i] = 1
        r[i] = lvl
        cnt += 1
        if i > 0 and not v[i-1]:
            nxt.append(i - 1)
        if i < n - 1 and not v[i+1]:
            nxt.append(i + 1)
        if not v[a[i]]:
            nxt.append(a[i])
    curr = nxt
    lvl += 1
print(' '.join(map(str,r)))