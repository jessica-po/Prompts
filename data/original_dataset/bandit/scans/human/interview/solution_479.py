n, k = map(int, input().split())
a = set(map(int, input().split()))
q = int(input())

# def isIn(x, fm, to):
# 	if fm >= to:
# 		return a[fm] == x
# 	t = a[(fm+to) // 2]
# 	if t > x:
# 		return isIn(x, fm, (fm+to) // 2 - 1)
# 	elif t < x:
# 		return isIn(x, (fm+to) // 2 + 1, to)
# 	else:
# 		return True

for _ in range(q):
	x = int(input())
	if x in a:
		print(1)
		continue
	found = False
	for i in range(2, k + 1):
		for j in range(1, i // 2 + 1):
			for l in a:
				t = x - l * j
				if t % (i - j) != 0:
					continue
				# if isIn(t // (i - j), 0, n - 1):
				if t // (i - j) in a:
					print(i)
					found = True
					break
			if found:
				break
		if found:
			break
	if not found:
		print(-1)