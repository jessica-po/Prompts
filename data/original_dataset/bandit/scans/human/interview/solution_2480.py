import bisect
N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
S=[0 for i in range(N+1)]
for i in range(N):
    S[i+1]=S[i]+A[i]
    S[i+1]%=K
X=[(S[i]-i)%K for i in range(N+1)]
D=dict()
for i in range(N+1):
    if X[i] in D:
        D[X[i]].append(i)
    else:
        D[X[i]]=[i]
ans=0
for k in D:
    for i in D[k]:
        L=bisect.bisect_left(D[k],i-K+1)
        R=bisect.bisect_right(D[k],i+K-1)
        ans+=R-L-1
print((ans//2))