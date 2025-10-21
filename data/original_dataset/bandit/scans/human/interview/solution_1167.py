from math import *


def ri():
    return int(input())


def rli():
    return list(map(int, input().split()))


q = ri()
for _ in range(q):
    a, b, c, d, k = rli()
    x = int(ceil(a / c))
    y = int(ceil(b / d))
    if x + y <= k:
        print(x, y)
    else:
        print(-1)