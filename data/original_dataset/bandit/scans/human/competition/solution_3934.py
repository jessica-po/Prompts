import getpass
import sys

if getpass.getuser() != 'frohenk':
    filename = 'half'
    # sys.stdin = open('input.txt')
    # sys.stdout = open('output.txt', 'w')
else:
    sys.stdin = open('input.txt')
    # sys.stdin.close()

import math
import string
import re
import random
from decimal import Decimal, getcontext
from collections import deque

mod = 10 ** 9 + 7


def ria():
    return [int(i) for i in input().split()]


n=ria()[0]
ar=[0]*n
for i in range(n-1):
    a,b=ria()
    a-=1
    b-=1
    ar[a]+=1
    ar[b]+=1
print('NO' if ar.count(2) else 'YES')