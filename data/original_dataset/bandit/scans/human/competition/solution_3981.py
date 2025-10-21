import sys


# > 0 anti-clock, < 0 clockwise, == 0 same line
def orientation(p1, p2, p3):
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])


def dot(p1, p2, p3, p4):
    return (p2[0]-p1[0])*(p4[0]-p3[0]) + (p2[1]-p1[1])*(p4[1]-p3[1])


def theta(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if abs(dx) < 0.1 and abs(dy) < 0.1:
        t = 0
    else:
        t = dy/(abs(dx) + abs(dy))
        if abs(t) < 0.1 ** 10:
            t = 0
    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t

    return t*90


def dist_sq(p1, p2):
    return (p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1])


def chull(points):
    # let 0 element to be smallest, reorder elements
    pi = [x for x in range(len(points))]
    min_y = points[0][1]
    min_x = points[0][0]
    min_ind = 0
    for i in range(len(points)):
        if points[i][1] < min_y or points[i][1] == min_y and points[i][0] < min_x:
            min_y = points[i][1]
            min_x = points[i][0]
            min_ind = i
    pi[0] = min_ind
    pi[min_ind] = 0
    th = [theta(points[pi[0]], points[x]) for x in range(len(points))]
    pi.sort(key=lambda x: th[x])
    # process equals
    unique = [pi[0], pi[1]]
    for i in range(2, len(pi)):
        if th[pi[i]] != th[unique[-1]]:
            unique.append(pi[i])
        else:
            if dist_sq(points[pi[0]], points[unique[-1]]) < dist_sq(points[pi[0]], points[pi[i]]):
                unique[-1] = pi[i] # put max
    pi = unique
    stack = []
    for i in range(min(len(pi), 3)):
        stack.append(points[pi[i]])
    if len(stack) < 3:
        return stack
    for i in range(3, len(pi)):
        while len(stack) >= 2:
            o = orientation(stack[-2], stack[-1], points[pi[i]])
            if o > 0:
                stack.append(points[pi[i]])
                break
            elif o < 0:
                stack.pop()
            else:  # ==
                if dist_sq(stack[-2], stack[-1]) < dist_sq(stack[-2], points[pi[i]]):
                    stack.pop()
                else:
                    break  # skip i-th point
    return stack


def z_func(s):
    slen, l, r = len(s), 0, 0
    z = [0]*slen
    z[0] = slen
    for i in range(1, slen):
        if i <= r: z[i] = min(r-i+1, z[i-l])
        while i+z[i] < slen and s[z[i]] == s[i+z[i]]: z[i] += 1
        if i+z[i]-1 > r: l, r = i, i+z[i]-1
    return z

n,m = map(int, sys.stdin.readline().strip().split())
a = []
for _ in range(n):
    x,y = map(int, sys.stdin.readline().strip().split())
    a.append((x, y))
b = []
for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    b.append((x, y))

ah = chull(a)
bh = chull(b)
if len(ah) == len(bh):
    if len(ah) == 2:
        if dist_sq(ah[0], ah[1]) == dist_sq(bh[0], bh[1]):
            print('YES')
        else:
            print('NO')
    else:
        da = []
        for i in range(len(ah)):
            dot_a = dot(ah[i-2], ah[i-1], ah[i-1], ah[i])
            da.append((dist_sq(ah[i], ah[i-1]), dot_a))
        db = []
        for i in range(len(bh)):
            dot_b = dot(bh[i - 2], bh[i - 1], bh[i - 1], bh[i])
            db.append((dist_sq(bh[i], bh[i-1]), dot_b))
        l = r = 0
        daab = []
        daab.extend(db)
        daab.append(-1)
        daab.extend(da)
        daab.extend(da)
        zab = z_func(daab)
        found = False
        for i in range(len(db)+1, len(daab)-len(db)+1):
            if zab[i] == len(db):
                found = True
                break
        if found:
            print('YES')
        else:
            print('NO')
else:
    print('NO')