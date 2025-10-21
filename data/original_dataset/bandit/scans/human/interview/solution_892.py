import sys

n, m = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B, C = [0]*(m+1), [0]*(m+1)
for a in A:
    if a <= m: B[a] += 1
for i in range(2, m + 1):
    for j in range(i, m+1, i):
        C[j] += B[i]

k, l = 1, 0
for i in range(2, m+1):
    if C[i] > l:
        l = C[i]
        k = i
print(k, l + B[1])
for i, a in enumerate(A):
    if k%a == 0: sys.stdout.write(str(i+1) + ' ')