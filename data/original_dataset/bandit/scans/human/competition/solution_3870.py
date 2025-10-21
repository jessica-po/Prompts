n, m = map(int, input().split())
u = [[], []]

for q in range(n):
    p, s = input().split()
    u[p == 'ATK'].append(int(s))

d, a = [sorted(q) for q in u]
v = sorted(int(input()) for q in range(m))
k, s = 0, sum(v)

i = j = 0
for q in v:
    if i < len(d) and q > d[i]:
        s -= q
        i += 1
    elif j < len(a) and q >= a[j]:
        s -= a[j]
        j += 1
if i + j - len(a) - len(d): s = 0
for q in v:
    if k < len(a) and q >= a[k]: k += 1

x = y = 0
v.reverse()
for i in range(k):
    x += a[i]
    y += v[i]
    s = max(s, y - x)
print(s)