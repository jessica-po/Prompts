import collections

class Graph:
	def __init__(self, n, dir):
		self.node_cnt = n
		self.__directed = dir
		self.__adjList = []
		for i in range(n): self.__adjList.append([])

	def addEdge(self, u, v):
		self.__adjList[u].append(v)
		if not self.__directed: self.__adjList[v].append(u)
	
	def getDistances(self, start, end=None):
		assert (0 <= start and start < self.node_cnt)
		dist = [-1] * self.node_cnt

		q = collections.deque()
		dist[start] = 0
		q.append(start)
		while len(q) > 0:
			z, breakable = q.popleft(), False
			if end == z: break
			for t in self.__adjList[z]:
				if dist[t] == -1:
					dist[t] = dist[z] + 1
					q.append(t)
					if t == end:
						breakable = True
						break
			if breakable: break
		
		return dist

def getAffectedDiameter(graph, affected):
	affection = [False for i in range(graph.node_cnt)]
	for x in affected: affection[x] = True
	dist0 = graph.getDistances(affected[0])
	affect_1 = -1
	for i in range(n):
		if affection[i] and (affect_1 == -1 or dist0[affect_1] < dist0[i]):
			affect_1 = i
	
	dist1 = graph.getDistances(affect_1)
	affect_2 = -1
	for i in range(n):
		if affection[i] and (affect_2 == -1 or dist1[affect_2] < dist1[i]):
			affect_2 = i
	
	return affect_1, affect_2

n, m, d = map(int, input().split())
p = list(map(lambda s: int(s)-1, input().split()))
g = Graph(n, dir=False)
for i in range(1, n):
	a, b = map(lambda s: int(s)-1, input().split())
	g.addEdge(a, b)

p1, p2 = getAffectedDiameter(g, p)
d1, d2 = g.getDistances(p1), g.getDistances(p2)

cnt = 0
for i in range(n):
	if d1[i] <= d and d2[i] <= d: cnt += 1
print(cnt)