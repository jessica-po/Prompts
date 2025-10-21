import sys

in1 = sys.stdin.readlines()
N = int(in1[0])
#N = 10 ** 18
#N = 2
"""
0 + 0 = 0
0 x 0 = 0

1 + 0 = 1
1 x 0 = 1

2 + 0 = 2
2 x 0 = 2
1 + 1 = 2
1 x 1 = 0

3 + 0 = 3
3 x 0 = 3
2 + 1 = 3
2 x 1 = 3
"""
p = 10 ** 9 + 7

def f(n):
    if n in d:
        return d[n]
    d[n] = f(n // 2) + f((n - 1) // 2) + f((n - 2) // 2)
    return d[n]

d = {0: 1, 1: 2}
print((f(N) % p))