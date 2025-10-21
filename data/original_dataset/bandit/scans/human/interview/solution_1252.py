def __starting_point():
	n, m, t = map(int, input().split())
	edge = {i:{} for i in range(n)}
	income = [0 for i in range(n)]
	for i in range(m):
		u, v, ti = map(int, input().split())
		edge[v-1][u-1] = ti
		income[u-1] += 1
	stat = [{} for _ in range(n)]
	stat[n-1] = {1 : (0, -1)}
	queue = [n-1]
	first = 0
	last = 1
	for i in range(n-2, 0, -1):
		if income[i] == 0:
			queue.append(i)
			last += 1
	while (first < last):
		v = queue[first]
		first += 1
		for u in edge[v].keys():
			income[u] -= 1
			for vis in stat[v].keys():
				cost = stat[v][vis][0] + edge[v][u]
				ucost = stat[u].get(vis+1, (t+1,-1))[0]
				if ucost > cost:
					stat[u][vis+1] = (cost, v)
			if income[u] <= 0:
				queue.append(u)
				last += 1
	#print(queue, last)
	res = max(stat[0].keys())
	print(res)
	path = []
	curr = 0
	path.append(curr+1)
	while(stat[curr][res][1] >= 0):
		curr = stat[curr][res][1]
		path.append(curr+1)
		res -= 1
	print(' '.join(map(str, path)))
__starting_point()