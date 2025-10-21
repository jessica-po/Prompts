t=int(input())
for t in range(t):
	n=int(input())
	s=input()
	a=[int(x) for x in s]
	p=a[n-1]
	print(str(p)*n)