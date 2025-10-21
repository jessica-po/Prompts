a, b, c, d = list(map(int, input().split(' ')))

ans = -(d+1) * (d+2) * (d+3) // 6
for l1 in range(0, d+1):
    minx = min(d-l1, a-b-c+l1)
    if minx < 0:
        continue;
    else:
        ans += (minx + 1) * (minx + 2) // 2

a, b, c = b, c, a
for l1 in range(0, d+1):
    minx = min(d-l1, a-b-c+l1)
    if minx < 0:
        continue;
    else:
        ans += (minx + 1) * (minx + 2) // 2

a, b, c = b, c, a
for l1 in range(0, d+1):
    minx = min(d-l1, a-b-c+l1)
    if minx < 0:
        continue;
    else:
        ans += (minx + 1) * (minx + 2) // 2

print(-ans)