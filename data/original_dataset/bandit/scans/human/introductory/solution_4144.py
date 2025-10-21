n = int(input())
mod = 10**9 + 7
all09 = ((2 * 10**n) % mod - (2 * 9**n) % mod) % mod
of09 = ((10**n) % mod - 8**n % mod) % mod
print((all09-of09)%mod)