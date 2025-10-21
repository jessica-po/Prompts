n = int(input())

A = list(map(int, input().split()))

maxDist = [0] * n

G = [[] for _ in range(n)]

for v in range(1, n):
    u, d = tuple(map(int, input().split()))
    u -= 1
    G[v].append((u, d))
    G[u].append((v, d))


seen = [False] * n
seen[0] = True
q = [0]
to_remove = []

while q:
    v = q.pop();
    for u, dist in G[v]:
        if not seen[u]:
            seen[u] = True
            maxDist[u] = max(dist, maxDist[v] + dist)
            if maxDist[u] > A[u]:
                to_remove.append(u)
            else:
                q.append(u)

count = 0
while to_remove:
    v = to_remove.pop()
    count += 1
    for u, _ in G[v]:
        if not seen[u]:
            seen[u] = True
            to_remove.append(u)

print(count)