n = int(input())
a = sum(list(map(int, input().split())))
if n == 1:
	if a == 1:
		print("YES")
	else:
		print("NO")
else:
	if a == n - 1:
		print("YES")
	else:
		print("NO")