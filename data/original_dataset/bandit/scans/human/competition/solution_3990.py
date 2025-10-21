from collections import deque
n,m=map(int,input().split())
a=[set() for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())  
    a[x].add(y)
    a[y].add(x)
if n not in a[1]:
    t=True
else:
    t=False
q=deque()
q.append(1)
z = [-1 for i in range(n+1)]
z[1] = 0
while len(q) > 0:
    v = q.popleft()
    for i in range(1, n+1):
        if t ^ (i in a[v]):
            continue
        if z[i]==-1:
            z[i]=z[v]+1
            q.append(i)
            if i == n:
                print(z[i])
                return
print(-1)