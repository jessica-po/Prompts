from math import sqrt
from fractions import gcd
l, r, x, y = list(map(int, input().split()))
if y % x != 0:
    print(0)
    return
lo = (l + x - 1) // x
hi = r // x
p = y // x
s = 0

k1 = 1
while k1 * k1 <= p:
    k2 = p // k1
    if lo <= k1 <= hi and lo <= k2 <= hi and gcd(k1, k2) == 1 and k1 * k2 == p:
        s += 1 + (k1 != k2)
    k1 += 1
print(s)