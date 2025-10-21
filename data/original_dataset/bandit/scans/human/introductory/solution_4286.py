import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
A=list(map(int,input().split()))

SP=[list(map(int,input().split())) for i in range(m)]

MIN=min(A)
x=A.index(MIN)
EDGE_x=[[x+1,i+1,A[x]+A[i]] for i in range(n) if x!=i]

EDGE=EDGE_x+SP

EDGE.sort(key=lambda x:x[2])

#UnionFind

Group=[i for i in range(n+1)]

def find(x):
    while Group[x] != x:
        x=Group[x]
    return x

def Union(x,y):
    if find(x) != find(y):
        Group[find(y)]=Group[find(x)]=min(find(y),find(x))

ANS=0
for i,j,x in EDGE:
    if find(i)!=find(j):
        ANS+=x
        Union(i,j)

print(ANS)