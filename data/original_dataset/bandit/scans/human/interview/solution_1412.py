from heapq import heappop, heappush

n, k = [int(x) for x in input().split()]
cs = []
for i in range(n):
    l, r = [int(x) for x in input().split()]
    cs.append((l, r, i+1))
cs.sort()
h = []
lcs = set()
for i in range(k-1):
    heappush(h, [cs[i][1], cs[i][2]])
    lcs.add(cs[i][2])
l = -1
poped = []
push_i = k-1
for i in range(k-1, n):
    heappush(h, [cs[i][1], cs[i][2]])
    d = h[0][0] - cs[i][0]
    if d > l:
        l = d
        for j in range(push_i, i+1):
            lcs.add(cs[j][2])
        for e in poped:
            lcs.remove(e)
        push_i = i+1
        poped = []
    poped.append(heappop(h)[1])

print(l+1)
if l == -1:
    for i in range(1, k+1):
        print(i, end=' ')

else:
    for i in lcs:
        print(i, end=' ')