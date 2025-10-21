q = int(input())

def racunaj():
	s = []
	for i in range(27):
		d = 2
		n = 2**i - 1
		z = 1
		while d*d <= n:
			if n % d == 0:
				z = n // d
				break
			d += 1
		s.append(z)
	return s

najdel = racunaj()
# print(najdel)

for _q in range(q):
	n = int(input())
	z = 1
	c = 1
	while z < n:
		z = 2*z+1
		c += 1
	if z > n:
		print(z)
	else:
		print(najdel[c])