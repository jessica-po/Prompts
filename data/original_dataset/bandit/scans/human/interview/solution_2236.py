import collections

n = int(input())
A = list(map(int, input().split()))
S = [0]*n

S[0] = A[0]
for i in range(1, n) :
    S[i] = S[i-1] + A[i]

C = collections.Counter(S)
max_val = 0
for key in C :
    max_val = max(max_val, C[key])
ans = n - max_val
print(ans)