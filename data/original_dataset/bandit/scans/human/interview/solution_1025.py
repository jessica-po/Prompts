from fractions import gcd
from collections import defaultdict

def read_data():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return n, points

def solve(n, points):
    if n <= 2:
        return 0
    zeros = 0
    for i, (x, y) in enumerate(points[:-2]):
        zeros += count_zeros(i, x, y, points)
    return n * (n-1) * (n-2) // 6 - zeros

def count_zeros(i, x, y, points):
    slopes = defaultdict(int)
    for xj, yj in points[i + 1:]:
        dx = x - xj
        dy = y - yj
        d = gcd(dx, dy)
        slope = (dx/d, dy/d)
        slopes[slope] += 1
    zeros = 0
    for val in slopes.values():
        if val >= 2:
            zeros += val * (val - 1)
    return zeros // 2

n, points = read_data()
print(solve(n, points))