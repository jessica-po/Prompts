# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = io.StringIO(os.read(0, os.fstat(0).st_size).decode()).readline
ii = lambda:int(input())
kk=lambda:map(int,input().split())
# k2=lambda:map(lambda x:int(x)-1, input().split())
ll=lambda:list(kk())
n = ii()

parents, rank = [-1]*n, [0]*n
loc = [i for i in range(n)]
def findParent(x):
	stack = []
	curr = x
	while parents[curr] != -1:
		stack.append(curr)
		curr = parents[curr]
	for v in stack:
		parents[v] = curr
	return curr
def union(x, y):
	best = None
	xP, yP = findParent(x), findParent(y)
	if rank[x] < rank[y]: best=parents[xP] = yP;
	elif rank[x] > rank[y]: best=parents[yP] = xP
	else:
		best=parents[yP] = xP
		rank[xP]+=1
	if values[loc[best]] == 0:
		loc[best] = loc[xP] if yP is best else loc[yP]

a = kk()
values = [0]*n
tbp=[]
for x in kk(): values[x]+=1
for i in range(n):
	if values[i] == 0: union(i, (i+1)%n)
for v in a:
	p = loc[findParent((n-v)%n)]

	tbp.append((v+p)%n)
	values[p]-=1
	if values[p] == 0: union(p, (p+1)%n)
print(*tbp)