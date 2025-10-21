N, M, K = list(map(int, input().split()))
A = [int(a) for a in input().split()]
S = [0]
for a in A:
    S.append(S[-1]+M*a-K)
MI = [(10**50)] * M
ans = 0
for i in range(N+1):
    MI[i%M] = min(MI[i%M], S[i])
    for j in range(M):
        ans = max(ans, (S[i]-MI[(i-j)%M] - K*((-j)%M))//M)
print(ans)