from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque
from collections import Counter


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


n, m, d = readmap()
A = readlist()
Aind = dict([(A[i], i) for i in range(n)])
A.sort()

q = deque()
a = A[0]
ans = [0] * n
ans[Aind[a]] = 1
maxday = 1

q.append((a, 1))
for i in range(1, n):
    if A[i] > q[0][0] + d:
        ans[Aind[A[i]]] = q[0][1]
        q.append((A[i], q[0][1]))
        q.popleft()
    else:
        maxday += 1
        ans[Aind[A[i]]] = maxday
        q.append((A[i], maxday))

print(maxday)
print(" ".join(list(map(str, ans))))