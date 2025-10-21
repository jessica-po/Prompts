n,k = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
r = 0
ok = 1
while ok:
    L = [0 for _ in range(n)]
    for i in range(n):
        B[i] = B[i] - A[i]
        if B[i] < 0:
            L[i] = -B[i]
            B[i] = 0
    if sum(L) <= k:
        r += 1
        k = k - sum(L)
    else:
        ok = 0
print(r)