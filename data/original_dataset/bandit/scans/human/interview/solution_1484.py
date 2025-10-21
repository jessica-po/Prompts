from functools import lru_cache
N, K = list(map(int, input().split()))
P = 998244353
A = [K+100] + [int(a) for a in input().split()] + [K+j for j in range(1, 10)]
# A = [K+100] + [1, 2] + [-1 for a in range(N-4)] + [3,4]+ [K+j for j in range(1, 10)]

X = [[0,0] for _ in range(N//2+5)]
X[0][0] = 1
for i in range(1, N//2+2):
    X[i][0] = X[i-1][1]
    X[i][1] = (X[i-1][0] * (K-1) + X[i-1][1] * (K-2)) % P
    
Y = [[0,0] for _ in range(N//2+5)]
Y[0][1] = 1
for i in range(1, N//2+2):
    Y[i][0] = Y[i-1][1]
    Y[i][1] = (Y[i-1][0] * (K-1) + Y[i-1][1] * (K-2)) % P
    
def calc(l, a, b):
    if a > K and b > K:
        return (K * pow(K-1, l-1, P)) % P
    if a > K or b > K:
        return pow(K-1, l, P)
    if a == b:
        return X[l+1][0]
    else:
        return Y[l+1][0]



l = 0
ans = 1
for j in range(2):
    pre = K + 50 + j
    for i in range(j, N+5, 2):
        if A[i] == -1:
            l += 1
        elif l > 0:
            ans *= calc(l, pre, A[i])
            ans %= P
            pre = A[i]
            l = 0
        elif pre == A[i]:
            # print(A)
            ans = 0
            break
        else:
            pre = A[i]

print(ans%P)