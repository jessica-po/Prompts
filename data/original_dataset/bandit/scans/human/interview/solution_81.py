from math import gcd
a, b = list(map(int, input().split()))
if b < a:
    a, b = b, a
if a == b:
    print(0)
    return
c = b - a
i = 1
ans = a * b // gcd(a, b)

def get(x):
    A = (a + x - 1) // x * x
    B = A - a + b
    return A * B // gcd(A, B), A

r = 0
while i * i <= c:
    if c % i == 0:
        A, AA = get(i)
        B, BB = get(c // i)
        if A < ans:
            ans = A
            r = AA - a
        if B < ans:
            ans = B
            r = BB - a
        if A == ans:
            r = min(r, AA - a)
        if B == ans:
            r = min(r, BB - a)
    i += 1
print(r)