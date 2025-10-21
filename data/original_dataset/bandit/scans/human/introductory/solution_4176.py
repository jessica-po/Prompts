import math
a,b = list(map(int,input().split()))

def lcm(x,y):
    return (x * y) // math.gcd(x, y)

print((lcm(a,b)))