N=int(input())
P=[-1]+[int(i)-1 for i in input().split()]
X=[int(i) for i in input().split()]
Q=[[] for i in range(N)]
for i in range(1,N):
    Q[P[i]].append(i)
dp=[0 for i in range(N)]
INF=10**9+7
def solve(i):
    cur=[INF for j in range(X[i]+1)]
    cur[0]=0
    for j in Q[i]:
        solve(j)
        prv=[k for k in cur]
        cur=[INF for k in range(X[i]+1)]
        for acc in range(len(prv)):
            if prv[acc]<INF:
                if acc+X[j]<=X[i]:
                    cur[acc+X[j]]=min(cur[acc+X[j]],prv[acc]+dp[j])
                if acc+dp[j]<=X[i]:
                    cur[acc+dp[j]]=min(cur[acc+dp[j]],prv[acc]+X[j])
    dp[i]=min(cur)
solve(0)
if dp[0]<INF:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")