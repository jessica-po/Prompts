a, b = map(int, input().split())

if b - a > 10:
	print(0)
else:
	s = 1
	for i in range(a + 1, b + 1):
		s *= i
	print(str(s)[-1])