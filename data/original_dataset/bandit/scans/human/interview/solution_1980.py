import sys
it = iter(sys.stdin.readlines())
input = it.__next__
n, k = list(map(int, input().split()))
d, c = [0] * n, [0] * n
for i in range(n):
    a, b = list(map(int, input().split()))
    d[i], c[i] = a, k - b

p, r, pre, suf, sm, mx = list(range(n)), [0] * n, c[:], c[:], c[:], c[:]

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y, w):
    x, y = find(x), find(y)
    z = y if r[y] > r[x] else x
    r[x] += r[x] == r[y]
    mx[z] = max(mx[x], mx[y], suf[x] + pre[y])
    pre[z] = max(pre[x], sm[x] + pre[y])
    suf[z] = max(suf[x] + sm[y], suf[y])
    sm[z] = sm[x] + sm[y]
    p[x] = p[y] = z
    return mx[z] - w ** 2

ans = max(0, max(c))
for w, i in sorted((d[i + 1] - d[i], i) for i in range(n - 1)):
    ans = max(ans, union(i, i + 1, w))
print(ans)