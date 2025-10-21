q = int(input())
for irweewr in range(q):
	n = int(input())
	l = list(map(int,input().split()))
	l.sort()
	l.reverse()
	print(*l)