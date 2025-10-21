from sys import *

T = int(stdin.readline())
t = [int(s) for s in stdin.readline().split(' ')]

a = []
for i in range(T - 1, -1, -1):

    if i % 2 == 0:
        a += [(e[0], -e[1]) for e in a]
        a = [(e[0] - t[i], e[1]) for e in a]
        a += [(- x - 1, 0) for x in range(t[i])]
        a = list(set(a))

    if i % 2 == 1:
        a += [(e[1], -e[0]) for e in a]
        a = [(e[0] - t[i], e[1] + t[i]) for e in a]
        a += [(- x - 1, x + 1) for x in range(t[i])]
        a = list(set(a))

print(len(a))