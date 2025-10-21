from heapq import heappush, heappop
queue = []
degree = []
s = []
ans = []
n = int(input())
used = [False for i in range(n)]
for i in range(n):
    a, b = list(map(int, input().split()))
    degree.append(a)
    s.append(b)
    heappush(queue, (a, i))
while queue:
    el = heappop(queue)
    vert = el[1]
    if used[vert]:
        continue
    used[vert] = True
    if degree[vert] == 0:
        continue
    other = s[vert]
    ans.append((vert, other))
    s[other] ^= vert
    degree[other] -= 1
    heappush(queue, (degree[other], other))
print(len(ans))
for el in ans:
    print(el[0], el[1])