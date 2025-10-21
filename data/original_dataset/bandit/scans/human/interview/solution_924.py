import sys
import string
from math import gcd
import getpass
import math
from decimal import Decimal
import pprint


def ria():
    return [int(i) for i in input().split()]


if getpass.getuser() != 'frohenk':
    filename = 'half'
    # sys.stdin = open('input.txt')
    # sys.stdout = open('output.txt', 'w')
else:
    sys.stdin = open('input.txt')
    # sys.stdin.close()
# sys.stdout = open('output.txt', 'w')


la, ra, ta = ria()
lb, rb, tb = ria()
if ta > tb:
    la, ra, ta, lb, rb, tb = lb, rb, tb, la, ra, ta

gc = gcd(tb, ta)
if gc == 1:
    print(min(ra - la + 1, rb - lb + 1))
    return


def get(st):
    nonlocal la, ra, ta, lb, rb, tb
    lc = la + st
    rc = ra + st
    return max(min(rc, rb) - max(lc, lb) + 1, 0)


sta = la // gc
stb = lb // gc
fna = ra // gc
fnb = rb // gc

mx = 0

mx = max(mx, get((stb - sta) * gc))
mx = max(mx, get((stb - sta + 1) * gc))
mx = max(mx, get((stb - sta + 2) * gc))
mx = max(mx, get((stb - sta - 1) * gc))
mx = max(mx, get((stb - sta - 2) * gc))

mx = max(mx, get((fnb - fna) * gc))
mx = max(mx, get((fnb - fna + 1) * gc))
mx = max(mx, get((fnb - fna + 2) * gc))
mx = max(mx, get((fnb - fna - 1) * gc))
mx = max(mx, get((fnb - fna - 2) * gc))

#print(stb - sta)
print(mx)