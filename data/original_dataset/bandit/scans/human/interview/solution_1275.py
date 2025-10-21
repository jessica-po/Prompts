N, K = map(int, input().split())
def num_pair(m):
    if m<=N:
        return m-1
    return 2*N-m+1

K = abs(K)

ans = 0
for i in range(K+2,2*N+1):
    ans += num_pair(i)*num_pair(i-K)
    
print(ans)