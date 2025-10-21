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


n = read()
V = []
for _ in range(n-1):
    a, b = readmap()
    V.append(a)
    if b < n:
        print("NO")
        quit()

V.sort()

for i in range(n-1):
    if V[i] <= i:
        print("NO")
        quit()

used = [False] * (n+1)
tree = []
for i in range(n-1):
    v = V[i]
    if not used[v]:
        tree.append(v)
        used[v] = True
    else:
        for j in range(1, n+1):
            if not used[j]:
                tree.append(j)
                used[j] = True
                break
tree.append(n)

print("YES")
for i in range(n-1):
    print(tree[i], tree[i+1])