import sys
import math


a, b, n = list(map(int, str.split(sys.stdin.readline())))
s = lambda i: a + (i - 1) * b
S = lambda i: a * i + b * i * (i - 1) // 2
for _ in range(n):

    l, t, m = list(map(int, str.split(sys.stdin.readline())))
    # Si = a * r + b * r * (r - 1) / 2
    # Si = b / 2 * r ^ 2 - (b / 2 - a) * r
    # si = a + (i - 1) * b => (si - a) / b + 1 = i

    # (S(r) - S(l-1)) / t <= m
    # S(r) <= m * t + S(l-1)
    # b / 2 * r ^ 2 - (b / 2 - a) * r - m * t - S(l-1) <= 0
    # D = (b / 2 - a) ^ 2 + 4 * b / 2 * (m * t + S(l-1))
    d = (b / 2 - a) ** 2 + 4 * b / 2 * (m * t + S(l - 1))
    if d < 0:

        print(-1)
        continue

    r = min(
        math.floor((t - a) / b + 1),
        math.floor(((b / 2 - a) + math.sqrt(d)) / b)
    )
    if r < l:

        print(-1)

    else:

        print(r)