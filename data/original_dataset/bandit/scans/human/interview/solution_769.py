a, b, c = list(map(int, input().split()))

pos = 1
for i in range(1000000):
	d = (10 * a) // b
	a = (10 * a) % b
	if c == d:
		print(pos)
		return
	else:
		pos += 1
print(-1)