def bel(mask, bit):
    return (mask & (1 << bit)) != 0
read = lambda: map(int, input().split())
n, k = read()
f = [0] * 100
for i in range(n):
    cur = int(''.join(input().split()), 2)
    cur ^= (1 << k) - 1
    f[cur] = 1
ans = 'NO'
if k == 1:
    if f[1]:
        ans = 'YES'
if k == 2:
    f1 = f2 = 0
    for i in range(4):
        if f[i]:
            if bel(i, 0): f1 = 1
            if bel(i, 1): f2 = 1
    if f1 and f2:
        ans = 'YES'
if k == 3:
    p = [0] * 3
    for i in range(8):
        if f[i]:
            for j in range(3):
                if bel(i, j): p[j] = 1
    for i in range(8):
        if f[i]:
            if bel(i, 0) and bel(i, 1) and p[2]: ans = 'YES'
            if bel(i, 0) and p[1] and bel(i, 2): ans = 'YES'
            if p[0] and bel(i, 1) and bel(i, 2): ans = 'YES'
if k == 4:
    for i in range(16):
        if f[i]:
            for j in range(16):
                if f[j]:
                    if (i | j) == 15:
                        ans = 'YES'
print(ans)