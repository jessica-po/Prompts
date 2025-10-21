import sys
from collections import Counter
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))
geta = 10**9+7

Q = int(readline())
C = Counter()

Ans = [sum(A)] + [0]*Q
A = [0] + A
table = [geta] + [0]*N
for qu in range(1, Q+1):
    s, t, u = list(map(int, readline().split()))
    vn = s*geta + t
    res = 0
    cv = C[vn]
    if u != cv:
        if table[cv] <= A[cv]:
            res = 1
        table[cv] -= 1
        if table[u] < A[u]:
            res -= 1
        table[u] += 1
    C[vn] = u
    Ans[qu] = Ans[qu-1] + res
print('\n'.join(map(str, [max(1, a) for a in Ans[1:]])))