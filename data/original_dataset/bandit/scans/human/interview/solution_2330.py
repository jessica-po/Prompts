t = int(input())

for _ in range(t):
	n, m = map(int, input().split())

	a = list(map(int, input().split()))

	if n <= 2:
		print(-1)
		continue
	if m < n:
		print(-1)
		continue

	cost = 0
	edges = []
	for i in range(n):
		edges.append((i+1, (i+1)%n + 1))
		cost += 2 * a[i]

	s = sorted(range(n), key=lambda i: a[i])

	for i in range(m-n):
		edges.append((s[0]+1, s[1]+1))
		cost += a[s[0]] + a[s[1]]

	print(cost)
	for u, v in edges:
		print(u, v)