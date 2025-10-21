from fractions import gcd
n, m, x, y, a, b = map(int, input().split())
r = gcd(a, b)
a, b = a // r, b // r
r = min(n // a, m // b)
a, b = a * r, b * r
cx, cy = (a + 1) // 2, (b + 1) // 2
dx, dy = min(n - a, max(cx, x) - cx), min(m - b, max(cy, y) - cy)
print(dx, dy, a + dx, b + dy)