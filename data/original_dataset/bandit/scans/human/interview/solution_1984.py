def put():
    return list(map(int, input().split()))
def diff(x,y):
    ans = 0
    for i in range(n*m):
        if s[x][i]!= s[y][i]:
            ans+=1
    return ans
def find(i):
    if i==p[i]:
        return i
    p[i] = find(p[i])
    return p[i]
def union(i,j):
    if rank[i]>rank[j]:
        i,j = j,i
    elif rank[i]==rank[j]:
        rank[j]+=1
    p[i]= j
def dfs(i,p):
    if i!=0:
        print(i,p)
    for j in tree[i]:
        if j!=p:
            dfs(j,i)

n,m,k,w = put()
s = ['']*k 
for i in range(k):
    for j in range(n):
        s[i]+=input()
edge = []
k+=1
rank = [0]*(k)
p = list(range(k))
cost = 0
tree = [[] for i in range(k)]

for i in range(k):
    for j in range(i+1,k):
        if i==0:
            z=n*m
        else:
            z = diff(i-1,j-1)*w
        edge.append((z,i,j))

edge.sort()
for z,i,j in edge:
    u = find(i)
    v = find(j)
    if u!=v:
        union(u,v)
        cost+= z
        tree[i].append(j)
        tree[j].append(i)

print(cost)
dfs(0,-1)