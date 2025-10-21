n,k = map(int, input().split())
P = list(map(int, input().split()))
e = []
for i in P:
    e.append((i+1)/2)
cumsum = [0]*(n+1)
for i in range(1,n+1):
    cumsum[i] = cumsum[i-1]+e[i-1]
k_sum = cumsum.copy()
for i in range(n+1):
    if i>=k:
        k_sum[i] -= cumsum[i-k]
print(max(k_sum[k-1:]))