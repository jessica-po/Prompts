N, I = list(map(int, input().split()))
A = sorted([int(a) for a in input().split()])
B = []
j = 0
for i in range(N):
    if i == 0 or A[i] == A[i-1]:
        B.append(j)
    else:
        j += 1
        B.append(j)

def calc(k):
    K = 1<<k
    i = 0
    j = 0
    ma = 0
    while j < N:
        if B[j]-B[i] <= K - 1:
            ma = max(ma, j-i+1)
            j += 1
        else:
            i += 1
    return N-ma

ans = 10**100
for i in range(31):
    if i * N <= 8 * I:
        ans = min(ans, calc(i))

print(ans)