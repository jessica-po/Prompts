MAXN = 1000000000

n = int(input())
a = list(map(int, input().split()))

def solve1():	
	for i in range(n-1):
		if abs(a[i]-a[i+1]) != 1:
			return False
	print("YES\n%d %d" % (MAXN, 1))
	return True

def solve2():
	w = -1
	for i in range(n-1):
		d = abs(a[i]-a[i+1])
		if d != 1:
			if w == -1:
				w = d
			elif w != d:
				return False
	if w <= 0:
		return False
	for i in range(n-1):
		if abs(a[i]-a[i+1]) == 1 and (a[i]-1)//w != (a[i+1]-1)//w:
			return False
	print("YES\n%d %d" % (MAXN, w))
	return True

if solve1():
	pass
elif solve2():
	pass
else:
	print("NO")