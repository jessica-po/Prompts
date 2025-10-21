import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
n,w=map(int,input().split())
knap=[[] for i in range(4)]
w0,v=map(int,input().split())
knap[0].append(v)
for i in range(n-1):
    W,v=map(int,input().split())
    knap[W-w0].append(v)
for i in range(4):
    knap[i].sort(reverse=1)
    knap[i]=[0]+knap[i]
for i in range(4):
    for j in range(1,len(knap[i])):
        knap[i][j]+=knap[i][j-1]
ans=0
for a in range(len(knap[0])):
    for b in range(len(knap[1])):
        for c in range(len(knap[2])):
            for d in range(len(knap[3])):
                if w0*a+(w0+1)*b+(w0+2)*c+(w0+3)*d<=w:
                    ans=max(ans,knap[0][a]+knap[1][b]+knap[2][c]+knap[3][d])
print(ans)