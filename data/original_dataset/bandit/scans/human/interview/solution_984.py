from collections import deque

nodes = []
parents = []
values = []
broken = []
upperBound = []
lowerBound = []

n = int(input())

for _ in range(n):
    v, l, r = map(int, input().split())
    nodes.append((v, l - 1, r - 1))
    parents.append(-1)
    values.append(v)
    broken.append(False)
    upperBound.append(10 ** 9)
    lowerBound.append(-10 ** 9)

for i, (v, l, r) in enumerate(nodes):
    if l > -1:
        parents[l] = i
    if r > -1:
        parents[r] = i

root = -1
for i in range(n):
    if parents[i] == -1:
        root = i

proc = deque([root])
while len(proc) > 0:
    node = proc.popleft()
    v, l, r = nodes[node]
    if l > -1:
        proc.append(l)
        upperBound[l] = min(upperBound[node], v)
        lowerBound[l] = lowerBound[node]
        if not (lowerBound[l] <= nodes[l][0] <= upperBound[l]):
            broken[l] = True
    if r > -1:
        proc.append(r)
        upperBound[r] = upperBound[node]
        lowerBound[r] = max(lowerBound[node], v)
        if not (lowerBound[r] <= nodes[r][0] <= upperBound[r]):
            broken[r] = True
        
s = set([])
for v, b in zip(values, broken):
    if not b:
        s.add(v)

ans = 0
for v in values:
    if v not in s:
        ans += 1

print(ans)