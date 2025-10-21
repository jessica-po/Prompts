n = int(input())
points = [0] * n
D = {}
for i in range(n):
    points[i] = tuple(int(x) for x in input().split())

for i in range(n):
    for j in range(i+1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        u, v = x2 - x1, y2 - y1
        if u < 0 or u == 0 and v < 0:
            u, v = -u, -v
        if (u, v) in D:
            D[(u, v)] += 1
        else:
            D[(u, v)] = 1

S = sum(D[i] * (D[i] - 1) // 2 for i in D)
print(S // 2)