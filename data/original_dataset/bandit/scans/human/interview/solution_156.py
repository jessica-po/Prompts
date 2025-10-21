import math
x = int(input())

ans = 10**13
ab = [1, 1]
for i in range(1, int(x**(1/2))+1):
    if x % i == 0:
        a = x//i
        b = i

        g = math.gcd(a, b)
        a *= g
        b *= g
        if ans > max(a, b):
            ans = max(a, b)
            ab = [a, b]

print(ab[0], ab[1])