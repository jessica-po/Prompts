def main():
	p, k = list(map(int, input().split()))
	s = 1
	m = pow(10,9)+7
	if k == 0:
		s = pow(p,p-1,m)
	elif k == 1:
		s = pow(p,p,m)
	else:
		o = 1
		n = k
		while n != 1:
			n = k*n %p
			o += 1
		c = (p-1)//o
		s = pow(p,c,m)
	print(s%m)
main()