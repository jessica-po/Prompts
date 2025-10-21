from collections import deque
n,m = [int(x) for x in input().split()]
adj = [[] for x in range(n+1)]
for _ in range(1,n):
	a,b = [int(x) for x in input().split()]
	adj[a].append(b)
	adj[b].append(a)
chaos = [int(x) for x in input().split()]
s = chaos[0]
chaos = set(chaos)
cc = [0]*(n+1)
st = deque()
st.append((s,-1))
while len(st):
	u,e = st.pop()
	if u<0:
		if e>=0:
			cc[e] += cc[-u]
		continue
	if u in chaos:
		cc[u] +=1
	st.append((-u,e))
	
	for v in adj[u]:
		if v!=e:
			st.append((v,u))
	
#dfs(s,-1)
adj = [list([v for v in u if cc[v]>0]) for u in adj]
a = (s,0)
st = deque()
st.append((a[0],-1,0))
while len(st):
	u,e,h = st.pop()
	if h>a[1]:
		a = (u,h)
	elif h==a[1] and u<a[0]:
		a = (u,h)
	for v in adj[u]:
		if v!=e:
			st.append((v,u,h+1))
b = a
a = (a[0],0)
st = deque()
st.append((a[0],-1,0))
while len(st):
	u,e,h = st.pop()
	if h>a[1]:
		a = (u,h)
	elif h==a[1] and u<a[0]:
		a = (u,h)
	for v in adj[u]:
		if v!=e:
			st.append((v,u,h+1))
print(min(a[0],b[0]))
print(2*(n-cc.count(0))-a[1])