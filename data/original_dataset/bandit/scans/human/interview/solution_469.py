from math import *

r, h = list(map(int, input().split()))
d = h % r

if d * 2 < r:
    print(h // r * 2 + 1)
elif sqrt(3) * (r / 2) + r - 1e-6 <= d + r:
    print(h // r * 2 + 3)
else:
    print(h // r * 2 + 2)