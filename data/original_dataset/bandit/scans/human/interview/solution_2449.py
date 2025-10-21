MOD = 10**9 + 7
m, N = list(map(int, input().split()))

binom = [[1] + [0 for i in range(m)] for j in range(m + 1)]
for n in range(1, m + 1):
    for k in range(1, n + 1):
        binom[n][k] = (binom[n - 1][k] + binom[n - 1][k - 1]) % MOD

bell = [0 for n in range(m + 1)]
bell[0] = bell[1] = 1
for n in range(1, m):
    for k in range(n + 1):
        bell[n + 1] += bell[k] * binom[n][k]
        bell[n + 1] %= MOD
#print(bell)

bags = [0 for i in range(m)]
for it in range(N):
    for i, z in enumerate(input()):
        if z == '1':
            bags[i] |= (1 << it)
difs = set(bags)
sol = 1
for mask in difs:
    sol = sol * bell[bags.count(mask)] % MOD
print(sol)