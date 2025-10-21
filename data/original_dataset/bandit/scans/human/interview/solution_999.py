import math
import itertools


def ria():
    return [int(i) for i in input().split()]


mx = 0

sz = ria()[0]
mx1 = 0
mn1 = 2000000000

for i in range(sz):
    l, r = ria()
    mx1 = max(l, mx1)
    mn1 = min(r, mn1)

sz = ria()[0]
mx2 = 0
mn2 = 2000000000

for i in range(sz):
    l, r = ria()
    mx2 = max(l, mx2)
    mn2 = min(r, mn2)
#print(mx1,mn1,mx2,mn2)
mx = max(mx, mx1 - mn2)
mx = max(mx, mx2 - mn1)
print(mx)