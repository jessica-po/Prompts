a, b, c = sorted(map(int, input().split()))
if a > 3:
	print('NO')
elif a == 3:
	if b > 3:
		print('NO')
	elif b == 3:
		if c > 3:
			print('NO')
		else:
			print("YES")
elif a == 1:
	print('YES')
else:
	if b == 2:
		print('YES')
	elif b > 4:
		print('NO')
	elif b == 4:
		if c == 4:
			print('YES')
		else:
			print('NO')
	else:
		print('NO')