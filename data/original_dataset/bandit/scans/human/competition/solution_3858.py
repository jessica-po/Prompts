import sys
input = sys.stdin.readline
from fractions import gcd
from collections import Counter

"""
適当に部分集合Xをとり、凸包 S として、Sに1点計上すればよい
これだと2^N点得られる
ただし、凸包の面積が0となる場合が例外
空集合、1点の場合と、線分の場合を除外する

"""

MOD = 998244353
N = int(input())
XY = [[int(x) for x in input().split()] for _ in range(N)]

answer = pow(2,N,MOD)
answer -= N + 1# 空、1点
for i,(x,y) in enumerate(XY):
    # i を選び、i+1番目以上のうちいくつかを選んで線分とする
    pts = []
    for x1, y1 in XY[i+1:]:
        dx, dy = x1-x, y1-y
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        # 標準化
        if dx < 0:
            dx, dy = -dx, -dy
        elif dx == 0:
            dy = 1
        pts.append((dx,dy))
    c = Counter(pts)
    for v in c.values():
        answer -= pow(2,v,MOD) - 1

answer %= MOD
print(answer)