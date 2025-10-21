from math import gcd


def f(x):
    return x - (x // C + x // D - x // lcm)


A, B, C, D = list(map(int, input().split()))
lcm = C * D // gcd(C, D)
print((f(B) - f(A - 1)))