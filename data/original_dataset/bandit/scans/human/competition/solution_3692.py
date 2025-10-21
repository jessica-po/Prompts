from math import sqrt
def pt(x):
    print(x)
rd = lambda: map(int, input().split())
n = int(input())
def f(x1, y1, r1, x2, y2, r2):
    a = (r1 + r2) ** 2
    b = (r1 - r2) ** 2
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if d > a:
        return 1
    elif d == a:
        return 4
    elif d < b:
        return 3
    elif d == b:
        return 5
    else:
        return 2
def g(x1, y1, r1, x2, y2, r2):
    ds = (x1 - x2) ** 2 + (y1 - y2) ** 2
    d = sqrt(ds)
    A = (r1 ** 2 - r2 ** 2 + ds) / (2 * d)
    h = sqrt(r1 ** 2 - A ** 2)
    x = x1 + A * (x2 - x1) / d  
    y = y1 + A * (y2 - y1) / d
    x3 = x - h * (y2 - y1) / d  
    y3 = y + h * (x2 - x1) / d
    x4 = x + h * (y2 - y1) / d  
    y4 = y - h * (x2 - x1) / d
    return x3, y3, x4, y4 
if n is 1:
    pt(2)
if n is 2:
    x1, y1, r1 = rd()
    x2, y2, r2 = rd()
    a = f(x1, y1, r1, x2, y2, r2)
    pt(4 if a is 2 else 3)
if n is 3:
    x1, y1, r1 = rd()
    x2, y2, r2 = rd()
    x3, y3, r3 = rd()
    a = f(x1, y1, r1, x2, y2, r2)
    b = f(x1, y1, r1, x3, y3, r3)
    c = f(x3, y3, r3, x2, y2, r2)
    t = [a, b, c]
    t.sort()
    a, b, c = t
    if a is 1 and b is 1 and c in [1, 3, 4, 5]:
        pt(4)
    if a is 1 and b is 1 and c is 2:
        pt(5)
    if a is 1 and b is 2 and c is 2:
        pt(6)
    if a is 1 and b is 2 and c in [3, 4, 5]:
        pt(5)
    if a is 1 and b in [3, 4, 5]:
        pt(4)
    if a is 2 and b is 2 and c is 2:
        x4, y4, x5, y5 = g(x1, y1, r1, x2, y2, r2)
        r = 8
        if abs((x4 - x3) ** 2 + (y4 - y3) ** 2 - r3 ** 2) < 1e-6:
            r -= 1
        if abs((x5 - x3) ** 2 + (y5 - y3) ** 2 - r3 ** 2) < 1e-6:
            r -= 1
        pt(r)
    if a is 2 and b is 2 and c is 3:
        pt(6)
    if a is 2 and b is 2 and c in [4, 5]:
        x4, y4, x5, y5 = g(x1, y1, r1, x2, y2, r2)
        if abs((x4 - x3) ** 2 + (y4 - y3) ** 2 - r3 ** 2) < 1e-6 or abs((x5 - x3) ** 2 + (y5 - y3) ** 2 - r3 ** 2) < 1e-6:
            pt(6)
        else:
            pt(7)
    if a is 2 and b is 3:
        pt(5)
    if a is 2 and b in [4, 5]:
        pt(6)
    if a is 3 and b in [3, 4, 5]:
        pt(4)
    if a is 4 and b is 4 and c is 4:
        pt(5)
    if a is 4 and b is 4 and c is 5:
        pt(4)
    if a is 4 and b is 5 and c is 5:
        pt(5)
    if a is 5 and b is 5 and c is 5:
        pt(4)