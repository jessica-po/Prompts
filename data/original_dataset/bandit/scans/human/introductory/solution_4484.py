import math
n, m = map(int, input().split())
mod = 10**9+7
if abs(n-m) > 1:
    print(0)
    return

dog = math.factorial(n)
monkey = math.factorial(m)
if abs(n-m) == 1:
    ans = dog*monkey % mod
elif n == m:
    ans = dog*monkey*2 % mod
print(ans%mod)