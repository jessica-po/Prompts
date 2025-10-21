n = int(input())
ans = 0
for i in range(1, n + 1):
	for j in range(i, n + 1):
		if 0 < i ^ j < n + 1 and i ^ j < i + j and i ^ j >= j:
			ans += 1
print(ans)