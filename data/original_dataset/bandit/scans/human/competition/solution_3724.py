n = int(input())
s = input()
s = list(map('_ABC'.index, s))
s0 = s[0]

MOD = 10 ** 9 + 7

dp = [0, 0, 0, 0]
dp[s0] = 1

p = 1
while p < n and s[p] == s0:
    p += 1

xor = 0 if p % 2 == 0 else s0

for i, c in enumerate(s[p:], start=p):

    d, e = c % 3 + 1, (c + 1) % 3 + 1

    dp[c] = sum(dp) % MOD
    dp[d], dp[e] = dp[e], dp[d]

    if i == p:
        dp[c] += p // 2
        dp[s[i - 1] ^ c] += (p - 1) // 2
    elif xor == 0:
        dp[c] += 1

    xor ^= c

print((sum(dp) % MOD))