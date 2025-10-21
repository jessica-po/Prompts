t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	n -= k**2
	if n<0:
		print("NO")
	elif n%2 == 0:
		print("YES")
	else:
		print("NO")