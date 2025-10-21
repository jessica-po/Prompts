T = int(input())

for _ in range(T):
	x = input()[::-1]
	y = input()[::-1]

	start = y.index("1")

	offset = x[start:].index("1")

	print(offset)