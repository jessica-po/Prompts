n,k=list(map(int,input().split()))
M=10**9+7
print(k**~-k*pow(n-k,n-k,M)%M)