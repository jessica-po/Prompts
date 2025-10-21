import fractions

x, y, a, b = list(map(int, input().split()))
d = fractions.gcd(x, y)
d = x * y // d
print(b // d - (a - 1) // d)