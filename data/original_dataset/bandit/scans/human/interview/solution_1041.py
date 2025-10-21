#Circle of Numbers
import math

def centre(n, pts):
    x, y = 0, 0
    for j in [7,11,13,17,19,23,29,31,37,1193,1663,2711,4007,65537]:
        if math.gcd(n,j) == 1:
            for i in range(n):
                k = int(pts[i])
                x += k*math.cos(math.pi * 2*i*j/n)
                y += k*math.sin(math.pi * 2*i*j/n)
            if not (abs(x) < 0.000001 and abs(y) < 0.000001):
                return 'NO'
    return 'YES'
    
def strconv(s):
    return [char for char in s]

n = int(input())
pts = strconv(input())
print(centre(n,pts))