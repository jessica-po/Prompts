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


n, m = ria()
ar = ria()
arc = []
art = []
res = []
for n, i in enumerate(ria()):
    if i == 1:
        art.append(ar[n])
        res.append(0)
    else:
        arc.append(ar[n])
nt = 0
for i in arc:
    while nt != len(art) - 1 and abs(art[nt] - i) > abs(art[nt + 1] - i):
        nt += 1
    res[nt] += 1

for i in res:
    print(i,end= ' ')