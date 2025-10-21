n = int(input())
points = set(int(x) for x in input().strip().split())
powers = [2**i for i in range(31)]

for point in points:
    for power in powers:
        if point + power in points and point + power + power in points:
            print(3)
            print(point, point + power, point + power + power)
            return

for point in points:
    for power in powers:
        if point + power in points:
            print(2)
            print(point, point + power)
            return

print(1)
print(points.pop())