import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list([int(x) - 1 for x in sys.stdin.readline().rstrip().split()])


# ===CODE===

def main():
    n, m = ns()
    e = [[] for _ in range(n)]
    for _ in range(m):
        l, r, d = ns()
        l, r = l - 1, r - 1
        e[l].append([r, d])
        e[r].append([l, -d])

    visited = [False] * n
    dist_mat = [INF] * n

    for i in range(n):
        if visited[i]:
            continue
        que = collections.deque()
        que.append([i, 0])
        visited[i] = True
        dist_mat[i] = 0
        while que:
            idx, dist = que.popleft()
            for ei, di in e[idx]:
                if visited[ei]:
                    if dist + di == dist_mat[ei]:
                        continue
                    else:
                        print("No")
                        return
                else:
                    visited[ei] = True
                    dist_mat[ei] = dist + di
                    que.append([ei, dist + di])

    print("Yes")


def __starting_point():
    main()

__starting_point()