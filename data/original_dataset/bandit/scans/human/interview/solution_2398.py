from math import *
for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    x, y, x1, y1, x2, y2 = map(int, input().split())
    x += b - a
    y += d - c
    if (x < x1 or x > x2 or y < y1 or y > y2):
        print("No")
        continue
    if x1 == x2 and x1 == x and (a != 0 or b != 0):
        print("No")
        continue
    if y1 == y2 and y1 == y and (c != 0 or d != 0):
        print("No")
        continue
    print("Yes")