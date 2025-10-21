import sys
from collections import deque


def main():
    N, p, q, *AB = list(map(int, sys.stdin.buffer.read().split()))
    p -= 1
    q -= 1

    G = [[] for _ in range(N)]
    for a, b in zip(*[iter(AB)] * 2):
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    if len(G[p]) == 1 and G[p][0] == q:
        print((0))
        return

    dist1 = [-1] * N
    dist1[p] = 0
    queue = deque([p])
    while queue:
        v = queue.popleft()
        for nv in G[v]:
            if dist1[nv] == -1:
                dist1[nv] = dist1[v] + 1
                queue.append(nv)

    dist2 = [-1] * N
    dist2[q] = 0
    queue = deque([q])
    while queue:
        v = queue.popleft()
        for nv in G[v]:
            if dist2[nv] == -1:
                dist2[nv] = dist2[v] + 1
                queue.append(nv)

    max_d = 0
    for d1, d2 in zip(dist1, dist2):
        if d1 < d2 and max_d < d2:
            max_d = d2

    print((max_d - 1))
    return


def __starting_point():
    main()

__starting_point()