import math

x, y = [int(v) for v in input().split()]

xly = x * math.log(y)
ylx = y * math.log(x)

if abs(xly - ylx) < 1e-8:
    print('=')
elif ylx < xly:
    print('<')
else:
    print('>')