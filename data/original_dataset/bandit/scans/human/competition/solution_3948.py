from collections import defaultdict

n, k = list(map(int, input().split()))

connections = defaultdict(set)

for _ in range(n-1):
	u, v = list(map(int, input().split()))
	connections[u].add(v)
	connections[v].add(u)

leafs = set()
for node in connections:
	if len(connections[node])==1:
		leafs.add(node)

steps = 0
is_correct = True
while is_correct and steps<=k:
	new_leafs = set()
	for x in leafs:
		if len(connections[x])>1:
			is_correct = False
			#print("Len of %d more than one"%x)
			break
		root = list(connections[x])[0]
		if len(connections[root])<4 and len(leafs)!=3:
			is_correct = False
			#print("x: %d Len of root %d less than three"%(x,root))
			#print(connections[root])
			break
	if not is_correct:
		break
	for x in leafs:
		root = list(connections[x])[0]
		new_leafs.add(root)
		connections[root].remove(x)
	leafs = new_leafs
	steps += 1
	if len(leafs)==1 and len(connections[list(leafs)[0]])==0:
		break

#print("steps is %d"%steps)
if is_correct and steps==k:
	print("Yes")
else:
	print('No')