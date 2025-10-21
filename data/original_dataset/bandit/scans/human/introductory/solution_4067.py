from sys import stdin, stdout
from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial
from random import randint

n = int(stdin.readline())
s = list(stdin.readline().strip())
a, b, c = s.count('0'), s.count('1'), s.count('2')
d = n // 3

for i in range(len(s)):
    if s[i] == '2' and c > d:
        if a < d:
            s[i] = '0'
            a += 1
            c -= 1
        else:
            s[i] = '1'
            b += 1
            c -= 1
    elif s[i] == '1' and b > d:
        if a < d:
            s[i] = '0'
            a += 1
            b -= 1

for i in range(len(s) - 1, -1, -1):
    if s[i] == '1' and b > d:
        if c < d:
            s[i] = '2'
            b -= 1
            c += 1
    elif s[i] == '0' and a > d:
        if c < d:
            s[i] = '2'
            a -= 1
            c += 1
        elif b < d:
            s[i] = '1'
            a -= 1
            b += 1


stdout.write(''.join(s))