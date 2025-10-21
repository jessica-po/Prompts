__author__ = 'sonerik'

import sys

inp = sys.stdin
# inp = open("a.txt")

p, q, l, r = map(int, inp.readline().strip().split())

z, x = [], []

for i in range(p):
    a_i, b_i = map(int, inp.readline().strip().split())
    z += [i for i in range(a_i, b_i+1)]

z_set = set(z)

for i in range(q):
    c_i, d_i = map(int, inp.readline().strip().split())
    x += [i for i in range(c_i, d_i+1)]

cnt = 0

for i in range(l, r+1):
    new_x = [j + i for j in x]
    new_x_set = set(new_x)
    if new_x_set.intersection(z_set):
        cnt += 1

print(cnt)