from math import gcd

n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    g = gcd(a, b)
    if g == 1:
        print("Finite")
    else:
        print("Infinite")