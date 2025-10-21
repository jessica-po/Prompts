inf = 10 ** 6
n = int(input())
a = list(map(int, input().split()))
dist = [inf] * n
for i in range(len(a)):
    if not a[i]:
        dist[i] = 0
        cur = 1
        i1 = i
        while i1 - 1 > - 1 and a[i1 - 1] != 0:
            dist[i1 - 1] = min(dist[i1 - 1], cur)
            i1 -= 1
            cur += 1
        i1 = i
        cur = 1
        while i1 + 1 < n and a[i1 + 1] != 0:
            dist[i1 + 1] = min(dist[i1 + 1], cur)
            i1 += 1
            cur += 1
print(*dist)