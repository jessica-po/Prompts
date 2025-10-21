n, m, x, y, z, p = list(map(int, input().split()))
n, m, x, y, z = n + 1, m + 1, x % 4, y % 2, (4 - z) % 4

def a(i, j, n, m, k):
    if k == 0: return i, j, n, m
    if k == 1: return j, n - i, m, n
    if k == 2: return n - i, m - j, n, m
    return m - j, i, m, n

def b(i, j, m, k):
    if k == 0: return i, j
    if k == 1: return i, m - j

for i in range(p):
    u, v = list(map(int, input().split()))
    u, v, q, p = a(u, v, n, m, x)
    u, v = b(u, v, p, y)
    u, v, q, p = a(u, v, q, p, z)
    print(u, v)