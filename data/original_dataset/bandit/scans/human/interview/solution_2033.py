n, m = list(map(int, input().split()))
prev_points = [[] for _ in range(n)]
for _ in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    prev_points[v].append(u)
k = int(input())
p = [int(pi) - 1 for pi in input().split()]
best_ways_d = [-1] * n
best_ways_nm1 = [0] * n
q = [(p[-1], 0)]
for u, d in q:
    if best_ways_d[u] < 0:
        best_ways_d[u] = d
        d += 1
        for v in prev_points[u]:
            q.append((v, d))
    elif best_ways_d[u] == d:
        best_ways_nm1[u] += 1
ans1 = ans2 = 0
for i in range(1, k):
    u, v = p[i - 1], p[i]
    if best_ways_d[u] <= best_ways_d[v]:
        ans1 += 1
        ans2 += 1
    elif best_ways_nm1[u]:
        ans2 += 1
print(ans1, ans2)