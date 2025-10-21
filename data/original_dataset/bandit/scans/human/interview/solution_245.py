n = int(input())
s = 0
INF = 10**9
minx = miny = INF
maxx = maxy = -INF

for i in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    s += abs(x1 - x2) * abs(y1 - y2)
    minx = min(minx, x1, x2)
    maxx = max(maxx, x1, x2)
    miny = min(miny, y1, y2)
    maxy = max(maxy, y1, y2)

if (maxx - minx) == (maxy - miny) and s == (maxx - minx) ** 2:
    print ("YES")
else:
    print ("NO")