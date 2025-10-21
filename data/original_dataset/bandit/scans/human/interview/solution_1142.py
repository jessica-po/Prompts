import sys

n, k = list(map(int, sys.stdin.readline().strip().split()))
L = []
R = []
A = []
for i in range (0, n):
    x = list(map(int, sys.stdin.readline().strip().split()))
    L.append(x[0])
    R.append(x[1])
    A.append(x[2])
L.append(R[-1])
i = n-1
x = 0
y = 0
ans = 0
v = True
N = [0 for i in range (0, n)]
while i >= 0:
    if R[i] == L[i+1]:
        x = max(x + A[i] - k * (R[i] - L[i]), 0)
        N[i] = x
    else:
        x = max(A[i] - k * (R[i] - L[i]), 0)
        N[i] = x
    if N[i] > k:
        v = False
    i = i - 1
m = k
N.append(0)
i = 0
while i < n and v == True:
    if m < N[i]:
        ans = ans + m
        m = k
    m = m - A[i]
    ans = ans + A[i]
    while m < 0:
        m = m + k
    i = i + 1
if v == True:
    print(ans)
else:
    print(-1)