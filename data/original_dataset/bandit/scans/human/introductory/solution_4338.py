from sys import stdin, stdout
from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial
from random import randint

n, x, y = map(int, stdin.readline().split())
values = list(map(int, stdin.readline().split()))

if x > y:
    stdout.write(str(n))
else:
    v = sum(map(lambda v: int(v <= x), values))
    stdout.write(str(v // 2 + (v & 1)))