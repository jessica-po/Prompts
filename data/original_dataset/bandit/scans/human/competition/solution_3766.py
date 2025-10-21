"""
Codeforces Round 253 Div 1 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""

def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return [int(x) for x in inputs.split()]

def write(s="\n"):
    if isinstance(s, list): s = " ".join(map(str,s))
    s = str(s)
    print(s, end="")

################################################### SOLUTION
import itertools
covers = itertools.product([0,1], repeat=10)

n, = read()
s = read(1)
a = [0] * 25
colors = "RGBYW"
for i in s:
    a[colors.index(i[0]) * 5 + int(i[1])-1] |= 1

def check(cover):
    nonlocal a
    unknowns = [0] * 11
    for i in range(25):
        if not a[i]: continue
        id = -1
        if not cover[i%5]: id = 5+i//5
        if not cover[5+i//5]:
            if id == -1:
                id = i%5
            else:
                id = 10
        if id > -1:
            if unknowns[id]: return False
            unknowns[id] = 1
    return True

mn = 99
for i in covers:
    if check(i):
        mn = min(mn, sum(i))

print(mn)