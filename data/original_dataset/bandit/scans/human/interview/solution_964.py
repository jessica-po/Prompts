import sys


def get_sol(a, b, c, n, reverse):
	#1
	if reverse[0]:
		a = (a[1], a[0], a[2])
	if reverse[1]:
		b = (b[1], b[0], b[2])
	if reverse[2]:
		c = (c[1], c[0], c[2])


	ans = []
	if a[0] == b[0] == c[0] == n:
		if a[1] + b[1] + c[1] == n:
			for i in range(a[1]):
				ans.append(a[2]*n)
			for i in range(b[1]):
				ans.append(b[2]*n)
			for i in range(c[1]):
				ans.append(c[2]*n)
			return True, ans
	if a[0] + c[0] == b[0] + c[0] == n and c[1] == n == a[1] + b[1]:
		for i in range(a[1]):
			ans.append(a[2]*a[0] + c[2] * c[0])
		for i in range(b[1]):
			ans.append(b[2]*b[0] + c[2] * c[0])
		return True, ans
	return False, ans

def printans(ans, n):
	print(n)
	for line in ans:
		print(line)
	return

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

x1, y1, x2, y2, x3, y3 = [int(i) for i in input().split()]
total_area = x1*y1 + x2*y2 + x3*y3
n = 0
while n ** 2 < total_area:
	n += 1
if n ** 2 != total_area:
	print(-1)
else:
	first = (x1, y1, 'A')
	second = (x2, y2, 'B')
	third = (x3, y3, 'C')
	pereb = (	(first, second, third),
				(first, third, second),
				(second, first, third),
				(second, third, first),
				(third, first, second),
				(third, second, first))
	for rev1 in (False, True):
		for rev2 in (False, True):
			for rev3 in (False, True):
				for per in pereb:
					reverse = (rev1, rev2, rev3)
					is_ans, ans = get_sol(per[0], per[1], per[2], n, reverse)
					if is_ans: printans(ans, n)
	
	
	print(-1)