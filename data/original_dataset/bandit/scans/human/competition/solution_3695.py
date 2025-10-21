n, t = map(int,input().split())
wait = list(map(int,input().split()))
seg = []
for i in range(n):
    # to get the food in wait[i], wait __ seconds before running
    m = max(0, wait[i]-i-1)
    M = t-i-2
    if m > M: continue
    seg.append((m, -1))
    seg.append((M, 1))
seg.sort()

ans = 0
cur = 0
for t, q in seg:
    cur-= q
    ans = max(ans, cur)
print(ans)