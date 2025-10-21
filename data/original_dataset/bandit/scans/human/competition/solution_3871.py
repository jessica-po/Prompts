import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
A=list(map(int,input().split()))
C=list(map(int,input().split()))
P=list(map(int,input().split()))

DP=[[-1<<30]*(n+1) for i in range(5001)]
# DP[k][cnt] = Aのmaxがkで, そういう人間がcnt人いるときのprofitの最大値

for i in range(5001):
    DP[i][0]=0

for i in range(n-1,-1,-1):
    a,c = A[i]-1,C[i]

    for j in range(n,-1,-1):
        if DP[a][j]==-1<<30:
            continue
        
        if DP[a][j] - c + P[a] > DP[a][j+1]:
            DP[a][j+1] = DP[a][j] - c + P[a]

            x, w=a, j+1
            while x+1<n+m:
                if DP[x+1][w//2] < DP[x][w] + w//2 * P[x+1]:
                    DP[x+1][w//2] = DP[x][w] + w//2 * P[x+1]

                    x,w=x+1,w//2
                else:
                    break

ANS=0
for i in range(5001):
    ANS=max(ANS,DP[i][0],DP[i][1])

print(ANS)