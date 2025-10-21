from math import inf
n, p = [int(x) for x in input().split()]
l = []
for i in range(n):
    a, b = [int(x) for x in input().split()]
    l.append((a, b, b/a))
l.sort(key=lambda x: x[2])
asum = 0
bsum = 0
sumt = 0
for i in range(n):
    a0, b0, _ = l[i]
    c1 = inf if i == n-1 else l[i+1][2]
    asum += a0
    bsum += b0
    dp = asum - p
    if dp > 0:
        t = bsum / dp
        if t < c1:
            print(t)
            return
print(-1)