import math
from functools import reduce
N = int(input())

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

A = []
for i in range(2, N+1):
    A.append(i)

X = lcm(*A) + 1
print(X)