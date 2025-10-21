from fractions import gcd
def lcm(a, b):
    return a*b//gcd(a, b)
n, a, b, p, q = list(map(int, input().split(' ')))
red = n//a
blue = n//b
if (p<q):
    red -= n//lcm(a, b)
else:
    blue -= n//lcm(a, b)

print(p*red+q*blue)