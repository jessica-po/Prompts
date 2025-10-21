import math
def dist(x, y, x1, y1, x2, y2):
    a = x-x1
    b = y-y1
    c = x2-x1
    d = y2-y1
    dot = a*c+b*d
    lensq = c*c+d*d
    param=-1
    if lensq != 0:
        param = dot / lensq
    if param < 0:
        xx = x1
        yy = y1
    elif param > 1:
        xx = x2
        yy = y2
    else:
        xx = x1 + param * c
        yy = y1 + param * d

    dx = x - xx
    dy = y - yy
    return (dx*dx+dy*dy)**0.5
def dist2(x, y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
import math
maxx = -1
minn = 100000000000000000
pts = []
a, b, c = list(map(int, input().split(' ')))
for i in range(a):
    x, y = list(map(int, input().split(' ')))
    pts.append([x, y])

k = []
for i in pts:
    k.append(dist2(i, [b, c]))
pts.append(pts[0])
for i in range(a):
    k.append(dist(b, c, pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1]))

print((max(k)**2-min(k)**2)*math.pi)