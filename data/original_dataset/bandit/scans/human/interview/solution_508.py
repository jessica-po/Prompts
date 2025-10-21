3

def read_ints():
	return [int(i) for i in input().split()]

n, a = read_ints()

res = 1

for i in range(2, n - 1):
	if abs(a - res * 180 / n) > abs(a - i * 180 / n):
		res = i

print(2, 1, res + 2)