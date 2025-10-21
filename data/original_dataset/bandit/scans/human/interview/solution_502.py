def read_ints():
	return [int(i) for i in input().split()]

coords = read_ints()
a, b, c = [(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]
def length_sqr(a, b):
	return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

if length_sqr(a, b) != length_sqr(b, c):
	print('No')
elif (c[0] - b[0]) * (b[1] - a[1]) == (c[1] - b[1]) * (b[0] - a[0]):
	print('No')
else:
	print('Yes')