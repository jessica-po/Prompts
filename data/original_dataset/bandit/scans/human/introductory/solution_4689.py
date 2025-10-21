k, n = map(int, input().split())
points = list(map(int, input().split()))

dist = []
for i in range(n):
    if i != n-1:
        distance = points[i+1] - points[i]
    else:
        distance = points[0]+k - points[i]
    dist.append(distance)

max = dist[0]
for j in range(1, len(dist), 1):
    if max < dist[j]:
        max = dist[j]
dist.remove(max)

ans = 0
for k in dist:
    ans += k
print(ans)