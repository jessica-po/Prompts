from collections import defaultdict
n, k = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
h = defaultdict(int)
for i in range(n):
	a[i + 1] ^= a[i]
for i in range(n + 1):
	h[min(a[i] ^ ((1 << k) - 1), a[i])] += 1
ans = 0
for x, t in list(h.items()):
	a = t // 2
	b = t - a
	ans += a * (a - 1) // 2 + b * (b - 1) // 2
ans = (n * (n + 1)) // 2 - ans
print(ans)