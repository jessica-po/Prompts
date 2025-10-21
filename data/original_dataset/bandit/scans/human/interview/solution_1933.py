n, m, k = map(int, input().split())
a = [[] for i in range(m)]
for i in range(n):
    b = [int(x) for x in input().split()]
    for j in range(m):
        a[j].append(b[j])
s = 0
p = 0
for i in range(m):
    a[i].append(0)
for i in a:
    d = 0
    ma = 0
    ans = 0
    cur = sum(i[:k - 1])
    for j in range(k - 1, n):
        if i[j]:
            cur += 1
        if cur > ma:
            ma = cur
            ans = d
        cur -= i[j - k + 1]
        d += i[j - k + 1]
    s += ma
    p += ans
print(s, p)