def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b, x, y = list(map(int, input().split()))

g = gcd(x, y)
x //= g
y //= g


print(min(a // x, b // y))