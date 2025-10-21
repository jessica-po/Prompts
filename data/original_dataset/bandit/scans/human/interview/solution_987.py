from collections import defaultdict
import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))


parent = [i for i in range(N)]
rank = [0] * N


def find(i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent[i])
        return parent[i]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


P = list(map(int, input().split()))
for i in range(M):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    unite(a, b)


d = defaultdict(list)
cnt = defaultdict(int)
for i in range(N):
    d[find(i)].append(P[i])

for i in range(N):
    if find(i) == i:
        d[i] = sorted(d[i], reverse=True)

ans = []
for i in range(N):
    k = find(i)
    ans.append(d[k][cnt[k]])
    cnt[k] += 1

print(' '.join(map(str, ans)))