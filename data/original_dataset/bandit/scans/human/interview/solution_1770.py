for _ in range(int(input())):
	n, x, y, d = map(int, input().split())
	tt = abs(x - y)
	if tt % d != 0:
		ans = -1
		if (y - 1) % d == 0:
			ans = (x - 1 + d - 1) // d + (y - 1) // d
		if (n - y) % d == 0:
			cc = (n - x + d - 1) // d + (n - y) // d
			if ans == -1 or cc < ans:
				ans = cc
		print(ans)
	else:
		print(tt // d)