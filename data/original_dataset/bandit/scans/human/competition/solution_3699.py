from math import *

ax, ay, bx, by, cx, cy = [int(t) for t in input().split()]
n = int(input())
dist = 0
maxv = [[-inf, -inf], [-inf, -inf]]
index = [[0,0], [0,0]]

def update(d, idx, p):
    nonlocal maxv, index
    if d > maxv[p][0]:
        maxv[p][1] = maxv[p][0]
        index[p][1] = index[p][0]
        maxv[p][0] = d
        index[p][0] = idx
    elif d > maxv[p][1]:
        maxv[p][1] = d
        index[p][1] = idx

for i in range(n):
    x, y = [int(t) for t in input().split()]
    bottle_recycle = sqrt((cx - x) ** 2 + (cy - y) ** 2)
    dist += bottle_recycle * 2
    dista = bottle_recycle - sqrt((ax - x) ** 2 + (ay - y) ** 2)
    distb = bottle_recycle - sqrt((bx - x) ** 2 + (by - y) ** 2)
    update(dista, i, 0)
    update(distb, i, 1)

ans = dist - maxv[0][0]
ans = min(ans, dist - maxv[1][0])
if(index[0][0] != index[1][0]):
    ans = min(ans, dist - maxv[0][0] - maxv[1][0])
elif(n > 1):
    ans = min(ans, dist - maxv[0][1] - maxv[1][0], dist - maxv[0][0] - maxv[1][1])
print(ans)