import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())
n = input()
a = listin()
odd = 0
even = 0
for i in a:
    if i%2:
        odd+=1
    else:
        even+=1
if (even == 0 or odd == 0):
    print(*a)
else:
    a.sort()
    print(*a)