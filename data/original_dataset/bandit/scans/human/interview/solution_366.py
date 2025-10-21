n, m =list(map(int, input().split()))
if m % n != 0:
	print( m // n + 1)
else:
	print(m // n)