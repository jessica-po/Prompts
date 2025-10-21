t = int(input())

for i in range(t):
	a, b = map(int, input().split())

	if a == 1:
		if b == 1:
			print('YES')
		else:
			print('NO')
		continue

	if a <= 3:
		if b <= 3:
			print('YES')
		else:
			print('NO')
		continue

	print('YES')