from math import ceil
def dist(x, y):
    return (x ** 2 + y ** 2) ** 0.5
r, x, y, x2, y2 = map(int, input().split())
print(ceil(dist(x - x2, y - y2) / (2 * r)))