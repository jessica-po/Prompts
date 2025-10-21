s = int(input(), 2)

t, ans = 1, 0

while t < s:
	ans += 1
	t *= 4

print(ans)