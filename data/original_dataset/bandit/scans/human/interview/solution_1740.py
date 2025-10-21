import sys
input = sys.stdin.readline

n=int(input())
P=[list(map(int,input().split())) for i in range(n-1)]


Group=[i for i in range(n+1)]
def find(x):
    while Group[x] != x:
        x=Group[x]
    return x
def Union(x,y):
    if find(x) != find(y):
        Group[find(y)]=Group[find(x)]=min(find(y),find(x))

ANS=[[i] for i in range(n+1)]

for i,j in P:
    if find(j)<find(i):
        ANS[find(j)]+=ANS[find(i)]
        
    else:
        ANS[find(i)]+=ANS[find(j)]

    Union(i,j)

for a in ANS[1]:
    print(a,end=" ")