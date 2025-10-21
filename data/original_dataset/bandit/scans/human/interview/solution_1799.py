from bisect import bisect_right
import heapq

n = int(input())
l = []

ti, wi = list(map(int, input().split()))
bal = ti
pos = 1
for _ in range(n - 1):
    ti, wi = list(map(int, input().split()))
    if ti > bal:
        pos += 1
    l.append((ti, wi - ti + 1))
l.sort()

best_pos = pos

op = bisect_right(l, (bal, float('inf')))
#print(l)

w = []
for i, v in l[op:]:
    heapq.heappush(w, v)
op -= 1

while w:
    head = heapq.heappop(w)
    if bal < head:
        break
    bal -= head
    pos -= 1

    #print(w, op)
    while op >= 0 and l[op][0] > bal:
        heapq.heappush(w, l[op][1])
        op -= 1
        pos += 1
    best_pos = min(best_pos, pos)

print(best_pos)