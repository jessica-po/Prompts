k, a, b = map(int, input().split())

mx_a = a // k
mx_b = b // k
if mx_a == 0 and b % k != 0:
	print(-1)
elif mx_b == 0 and a % k != 0:
	print(-1)
else:
	print(mx_a + mx_b)