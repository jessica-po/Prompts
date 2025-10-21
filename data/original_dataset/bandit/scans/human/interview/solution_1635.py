import itertools
import re
import math
import getpass
import sys

debug = False
files = False
if getpass.getuser() == 'frohe':
    debug = True

if debug and files:
    sys.stdin = open('test.in')


def ria():
    return [int(i) for i in input().split()]


n = ria()[0]
ar = ria()
mp = {}
for i in ar:
    mp[i] = 0
for n, i in enumerate(ar):
    mp[i] = n
mini = ar[0]
for i in mp:
    if mp[mini]>mp[i]:
        mini=i
print(mini)