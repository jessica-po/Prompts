from collections import defaultdict

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

u = defaultdict(int)
for i in b: u[i] += 1

ans = []
for q in range(p):
    c = a[q: n: p]
    if len(c) < m: break

    v = defaultdict(int)
    for i in c[: m]: v[i] += 1

    d = q + 1
    if u == v: ans.append(d)

    for j, k in zip(c[: len(c) - m], c[m: ]):
        v[j] -= 1
        if v[j] == 0: v.pop(j)
        v[k] += 1

        d += p
        if u == v: ans.append(d)

ans.sort()
print(len(ans))
print(' '.join(map(str, ans)))