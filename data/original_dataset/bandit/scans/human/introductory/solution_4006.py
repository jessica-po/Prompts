darling = {}
x = int(input())
ans = 0
while (x not in darling):
	darling[x] = 1
	ans += 1
	x += 1
	while (x % 10 == 0):
		x /= 10

print(ans)