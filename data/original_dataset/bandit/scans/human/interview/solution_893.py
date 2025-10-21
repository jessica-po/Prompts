f = lambda: map(int, input().split())
m = 1000000007

d, n = f()
t = list(f())
p = [[] for i in range(n)]
for j in range(n - 1):
    u, v = f()
    u -= 1
    v -= 1
    p[u].append(v)
    p[v].append(u)

def g(u, x, a, b, q):
    k = 1
    for v in p[u]:
        if a < t[v] <= b or t[v] == a and v > q:
            if v != x: k += k * g(v, u, a, b, q) % m
    return k


s = 0
for q in range(n):
    a = t[q]
    b = a + d
    s += g(q, -1, a, b, q)

print(s % m)