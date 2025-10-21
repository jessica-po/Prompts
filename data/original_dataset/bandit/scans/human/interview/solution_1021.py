n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def dif(x):
	c = []
	for i in range(n-1):
		c.append(x[i+1] - x[i])
	return c

if list(sorted(dif(a))) == list(sorted(dif(b))) and a[0] == b[0] and a[n-1] == b[n-1]:
	print('Yes')
else:
	print('No')