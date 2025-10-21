n = int(input())
if n <= 2:
	print("No")
else:
	print("Yes")
	print(1, (n + 1) // 2)
	ans = []
	for i in range(1, n + 1):
		if i != (n + 1) // 2:
			ans.append(i)
	print(n - 1, *ans)