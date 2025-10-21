def main():
	(n, k) = (int(x) for x in input().split())
	(a, b, c, d) = (int(x) for x in input().split())
	(path1, path2) = solver(n, k, a, b, c, d)
	if path1 == None:
		print(-1)
	else:
		for x in path1:
			print(x, end = ' ')
		print()
		for x in path2:
			print(x, end = ' ')

def solver(n, k, a, b, c, d):
	if k <= n or n == 4:
		return (None, None)
	else:
		path1 = [a, c] + \
		[i for i in range(1, n + 1) if i not in (a, b, c, d)] + \
		[d, b]
		path2 = [c, a] + \
		[i for i in range(1, n + 1) if i not in (a, b, c, d)] + \
		[b, d]
		return (path1, path2)

main()
#print(solver(7, 11, 2, 4, 7, 3))

# def reorder(path, n, a, b, c, d):
# 	for i in range(len(path)):
# 		if path[i] == a:
# 			path[i] = 1
# 		elif path[i] == b:
# 			path[i] = n
# 		elif path[i] == c:
# 			path[i] = 2
# 		elif path[i] == d:
# 			path[i] = 3
# 		elif path[i] == 1:
# 			path[i] = a
# 		elif path[i] == n:
# 			path[i] = b
# 		elif path[i] == 2:
# 			path[i] = c
# 		elif path[i] == 3:
# 			path[i] = d