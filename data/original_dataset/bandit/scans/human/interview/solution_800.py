3

import math

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
angles = sorted([math.atan2(x, y) for x, y in points])
angles.append(angles[0] + 2 * math.pi)
max_angle = max([abs(a - b) for a, b in zip(angles[:-1], angles[1:])] + [])
print('%0.9f' % (180 * (2 * math.pi - max_angle) / math.pi))