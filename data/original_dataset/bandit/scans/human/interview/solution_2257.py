import math
n, x1, y1, x2, y2 = [int(x) for x in input().split()]
points = []
for i in range(n):
    points.append(tuple(int(x) for x in input().split()))
d = lambda p1, p2: (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
first = (x1, y1)
second = (x2, y2)
distances = [(d(first, point), d(second, point)) for point in points]
distances.sort()
maxtaild = [0 for i in range(n+1)]
for i in range(n-1, -1, -1):
    maxtaild[i] = max(maxtaild[i+1], distances[i][1])
print(min(maxtaild[0], min(distances[i][0] + maxtaild[i+1] for i in range(n))))