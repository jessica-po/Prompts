from  math import gcd
n = int(input())
a=  list(map(int, input().split()))
k  = 0
for i in range(n):
    k = gcd(a[i], k)

ans = 0

def fact(n):
    nonlocal ans
    d = 1
    while d* d <= n:
        if n % d == 0:
            ans += 1
            if n // d != d:
                ans += 1
        d += 1
fact(k)
print(ans)