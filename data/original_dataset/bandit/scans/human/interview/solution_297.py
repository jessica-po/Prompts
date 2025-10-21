def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a


n, m, k = list(map(int, input().split()))
_n, _m = n, m
n, k = n // gcd(n, k), k // gcd(n, k)
m, k = m // gcd(m, k), k // gcd(m, k)
a = 2
a, k = a // gcd(a, k), k // gcd(a, k)
if k != 1:
    print("NO")
elif a * n <= _n:
    print("YES")
    print("0 0")
    print(a * n, 0)
    print(0, m)
elif a * m <= _m:
    print("YES")
    print("0 0")
    print(n, 0)
    print(0, m * a)
else:
    print("NO")