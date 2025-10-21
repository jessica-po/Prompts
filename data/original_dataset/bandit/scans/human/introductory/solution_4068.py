import sys

N, M = list(map(int, input().split()))

a = [False]*(N+1)
for i in range(M):
    a[int(input())] = True

b = [0]*(N+1)

if N < 2:
    print((1))
    return

b[-1] = 1

for i in reversed(list(range(0, N))):
    if a[i]:
        b[i] = 0
        continue
    if i == N-1:
        b[i] = b[i+1]
    else:
        b[i] = (b[i+1] + b[i+2])%(10**9+7)

print((b[0]))