# import getpass
import sys
import math

EPS = 0.000000001

files = True
debug = False

# if getpass.getuser() == 'frohenk' and files:
#     debug = True
#     sys.stdin = open("test.in")
#     # sys.stdout = open('test.out', 'w')
# elif files:
#     # fname = "gift"
#     # sys.stdin = open("%s.in" % fname)
#     # sys.stdout = open('%s.out' % fname, 'w')
#     pass


def lcm(a, b):
    return a * b // math.gcd(a, b)


def ria():
    return [int(i) for i in input().split()]


def range_sum(a, b):
    ass = (((b - a + 1) // 2) * (a + b))
    if (a - b) % 2 == 0:
        ass += (b - a + 2) // 2
    return ass


def comba(n, x):
    return (math.factorial(n) // math.factorial(n - x)) // math.factorial(x)


def eq(a, b):
    return abs(a - b) <= EPS


n, ta = ria()
vs = ria()
ts = ria()
ks = []
up = 0
down = sum(vs)
for i in range(n):
    ks.append((ts[i], vs[i]))
    up += ts[i] * vs[i]
ks.sort()
if up / down > ta:

    if min(ts)>ta:
        print('0')
        return

    ks = list(reversed(ks))

    for t, v in ks:
        if down == 0:
            print(0)
            return
        if eq(up / down, ta):
            print(down)
            return
        if (up - t * v) / (down - v) > ta or eq((up - t * v) / (down - v), ta):
            up -= t * v
            down -= v
            continue

        l, r = 0, v

        up -= t * v
        down -= v

        while r - l > EPS:
            m = (l + r)/2
            if (up + t * m) / (down + m)>ta:
                r=m
            else:
                l=m
        print(down+l)
        return


else:

    if max(ts) < ta:
        print('0')
        return
    for t, v in ks:
        if down == 0:
            print(0)
            return
        if eq(up / down, ta):
            print(down)
            return
        if (up - t * v) / (down - v) < ta or eq((up - t * v) / (down - v), ta):
            up -= t * v
            down -= v
            continue

        l, r = 0, v

        up -= t * v
        down -= v

        while r - l > EPS:
            m = (l + r)/2
            if (up + t * m) / (down + m)<ta:
                r=m
            else:
                l=m
        print(down+l)
        return