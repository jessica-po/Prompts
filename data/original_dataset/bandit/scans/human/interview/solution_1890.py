a = input()
k = int(input())
n = len(a)
ans = 0
MOD = 10 ** 9 + 7
m = 1 - pow(2, n * k, MOD)
m *= pow(1 - pow(2, n, MOD), MOD - 2, MOD)
m %= MOD
for i in range(n - 1, -1, -1):
    if a[i] == '0' or a[i] == '5':  
        ans += (m * pow(2, i, MOD)) % MOD
ans = ans % MOD
if ans < 0:
    ans += MOD
print(ans)