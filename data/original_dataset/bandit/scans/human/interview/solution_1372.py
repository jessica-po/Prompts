h, n = map(int, input().split())
a, b = [], []
for _ in range(n):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

a_max = max(a)
dp = [0]*(h+a_max)

for i in range(h+a_max):
    dp[i] = min(dp[i-a] + b for a, b in zip(a, b))

print(min(dp[h-1:]))