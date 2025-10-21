from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

sum_a, sum_b = sum(a), sum(b)
delta = sum_b - sum_a
ans = abs(delta)
ans_swap = []

for i in range(n):
    for j in range(m):
        if abs((sum_a - a[i] + b[j]) - (sum_b + a[i] - b[j])) < ans:
            ans = abs((sum_a - a[i] + b[j]) - (sum_b + a[i] - b[j]))
            ans_swap = [(i+1, j+1)]

d = dict()
for i in range(m):
    for j in range(i+1, m):
        d[b[i]+b[j]] = (i+1, j+1)

minf, inf = -10**13, 10**13
val = [minf, minf] + sorted(d.keys()) + [inf, inf]

for i in range(n):
    for j in range(i+1, n):
        ap = a[i] + a[j]
        req = (delta + ap*2) >> 1
        k = bisect_left(val, req)

        for k in range(k-1, k+2):
            if abs(delta + ap*2 - val[k]*2) < ans:
                ans = abs(delta + ap*2 - val[k]*2)
                ans_swap = [(i+1, d[val[k]][0]), (j+1, d[val[k]][1])]

print(ans)
print(len(ans_swap))
for x, y in ans_swap:
    print(x, y)