def mi():
	return map(int, input().split())

n,m = mi()
a = [0]*m
for i in range(n):
	l,r = mi()
	for i in range(l-1, r):
		a[i] = 1
print (a.count(0))
for i in range(m):
	if a[i]==0:
		print (i+1, end = ' ')