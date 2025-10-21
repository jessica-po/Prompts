f = lambda: map(int, input().split())
n, m = f()
t = list(f())
d = {i: j for j, i in enumerate(sorted(set(t)))}
t = [d[i] for i in t]
k = len(d)
a = [0] * k
if m < 2 * k:
    for j in t * m:
        a[j] += 1
        q = a[j]
        j += 1
        while j < k and a[j] < q:
            a[j] += 1
            j += 1
    print(a[-1])
    return
a = [0] * k
for j in t * k:
    a[j] += 1
    q = a[j]
    j += 1
    while j < k and a[j] < q:
        a[j] += 1
        j += 1
b = [0] * k
t.reverse()
for j in t * k:
    b[j] += 1
    q = b[j]
    j -= 1
    while j > -1 and b[j] < q:
        b[j] += 1
        j -= 1
print(max(a[j] + (m - 2 * k) * t.count(j) + b[j] for j in range(k)))