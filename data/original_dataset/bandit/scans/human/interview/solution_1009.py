n, k = list(map(int,input().split()))
L = list(map(int,input().split()))
i = 0
p = 0
z = 1
R = [0 for _ in range(k)]
while i<n:
    R[p] += L[n-1-i]
    p = p + z
    i+=1
    if p == k or p == -1:
        z = z*(-1)
        if p == k:
            p = p - 1
        else:
            p = p + 1
print(max(R))