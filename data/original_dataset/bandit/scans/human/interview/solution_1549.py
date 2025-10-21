from bisect import bisect_left as bl
import sys

N, M, Q = map(int, sys.stdin.readline().split())
count = [0] * (M + 1)
A = []
for a in sys.stdin.readline().split():
    a = int(a)
    A.append(count[a] * M + a)
    count[a] += 1
A.sort()
A = [a - i for i, a in enumerate(A, 1)]
for _ in range(Q):
    q = int(sys.stdin.readline()) - N
    if q > A[-1]:
        q += N
    else:
        q += bl(A, q)
    sys.stdout.write(f'{(q - 1) % M + 1}\n')