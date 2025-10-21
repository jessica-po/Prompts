import math
leftpeople = set()
rightpeople = set()

n, vl = list(map(int, input().split()))

def leftinterval(x0, v0, t):
    if x0 / v0 <= t:
        return (0, 10**6)
    if x0 / (vl + v0) > t:
        return (-1, -2)
    leftbound = x0
    rightbound = (vl * vl - v0 * v0) * t + x0 * v0
    rightbound /= vl
    rightbound = int(rightbound)
    if rightbound > 10**6:
        rightbound = 10**6
    return (leftbound, rightbound)
def rightinterval(x0, v0, t):
    if (10**6 - x0) / v0 <= t:
        return (0, 10**6)
    if (10**6 - x0) / (v0 + vl) > t:
        return (-1, -2)
    rightbound = x0
    leftbound = v0 * x0 + (10**6) * (vl - v0) - t * (vl * vl - v0 * v0)
    leftbound /= vl
    leftbound = math.ceil(leftbound)
    if(leftbound < 0):
        leftbound = 0
    return (leftbound, rightbound)

def check(t):
    events = []
    for item in leftpeople:
        temp = leftinterval(item[0], item[1], t)
        if(temp[0] > temp[1]):
            continue
        events.append((temp[0], 0, 0))
        events.append((temp[1], 1, 0))
        if(temp[1] - temp[0] == 10**6):
            break
    for item in rightpeople:
        temp = rightinterval(item[0], item[1], t)
        if(temp[0] > temp[1]):
            continue
        events.append((temp[0], 0, 1))
        events.append((temp[1], 1, 1))
        if(temp[1] - temp[0] == 10**6):
            break
    events.sort()
    opened = [0, 0]
    for item in events:
        color = item[2]
        action = item[1]
        if action == 0:
            if opened[(color + 1) % 2] > 0:
                return True
            opened[color] += 1
        else:
            opened[color] -= 1
    return False

for i in range(n):
    a, b, c = list(map(int, input().split()))
    if c == 1:
        leftpeople.add((a, b))
    if c == 2:
        rightpeople.add((a, b))

l = 0
r = 1e9
for i in range(50):
    m = (l + r) / 2
    if(check(m)):
        r = m
    else:
        l = m

print(m)