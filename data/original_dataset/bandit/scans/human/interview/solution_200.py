from math import *

h1, h2 = [int(i) for i in input().split()]
a, b = [int(i) for i in input().split()]
a *= 12
b *= 12
if a <= b and h2 - h1 > (a // 12 * 8):
    print(-1)
    return
h1 += (a // 12 * 8)
if h1 >= h2:
    print(0)
    return
day = int(ceil((h2 - h1) / (a - b)))
print(day)