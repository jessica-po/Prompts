import sys

a, b, c = list(map(int, input().split()))
if c - b + a < 0 or (c - b + a) % 2 == 1:
    print("Impossible")
    return
f = (c - b + a) // 2
e = b - a + f
d = a - f
if d < 0 or f < 0 or e < 0:
    print("Impossible")
    return    
print(d, e, f)