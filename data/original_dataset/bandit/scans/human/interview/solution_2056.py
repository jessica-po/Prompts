import sys
from copy import copy

input = sys.stdin.readline

n = int(input())
l = [int(a) for a in input().split()]
x = []
for i in range(0, 20):
    res = 0
    for a in l:
        if a & (1 << i):
            res += 1
    x.append(res)

res = 0
for i in range(n):
    a = 0
    for j in range(20):
        if i < x[j]:
            a += (1 << j)
    res += a ** 2
print(res)