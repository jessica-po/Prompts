import sys
from itertools import combinations
from math import sqrt
import numpy as np

read = sys.stdin.read
readline = sys.stdin.readline


def main():
    N, K, *xyc = list(map(int, read().split()))
    x = xyc[::3]
    y = xyc[1::3]
    xy = list(zip(x, y))
    c = xyc[2::3]
    left = 0
    right = 10 ** 6
    delta = 0.1 ** 7
    while right - left > delta:
        mid = (left + right) / 2
        intersections = []
        r = [(mid / i) ** 2 for i in c]
        for i, j in combinations(list(range(N)), 2):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            X = x2 - x1
            Y = y2 - y1
            XY = X ** 2 + Y ** 2
            r1 = r[i]
            r2 = r[j]

            a = (XY + r1 - r2) / 2
            b = XY * r1 - a ** 2
            if b < delta:
                continue
            b = sqrt(b)
            xi1 = (a * X + Y * b) / XY + x1
            yi1 = (a * Y - X * b) / XY + y1
            xi2 = (a * X - Y * b) / XY + x1
            yi2 = (a * Y + X * b) / XY + y1
            intersections.append((xi1, yi1))
            intersections.append((xi2, yi2))

        intersections.extend(xy)
        intersections = np.array(intersections, np.float)
        cnt = np.zeros(len(intersections), np.int64)

        for (i, j), k in zip(xy, r):
            XY = (intersections[:, 0] - i) ** 2 + (intersections[:, 1] - j) ** 2
            cnt[XY < k + delta] += 1

        if np.any(cnt >= K):
            right = mid
        else:
            left = mid

    print(right)


def __starting_point():
    main()

__starting_point()