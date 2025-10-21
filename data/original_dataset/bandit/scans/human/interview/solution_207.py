def read_ints():
	return [int(i) for i in input().split()]

n = read_ints()
a = read_ints()
if len(a) % 2 and a[0] % 2 and a[-1] % 2:
	print('Yes')
else:
	print('No')