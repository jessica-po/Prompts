import numpy as np
N, C = list(map(int, input().split()))

xv = [(0, 0)]
for i in range(N):
    x, v = list(map(float, input().split()))
    xv.append((x, v))

sumA = np.zeros(N+2, dtype=float)
sumB = np.zeros(N+2, dtype=float)

xv.sort(key=lambda tup:tup[0])
xv.append((C,0))

for i in range(N+1):
    sumA[i+1] = sumA[i] + xv[i+1][1]
    sumB[i+1] = sumB[i] + xv[N-i][1]

maxA = [0]*(N+1)
maxB = [0]*(N+1)
for i in range(N):
    if sumA[i+1] < xv[i+1][0]: sumA[i+1] = 0
    else: sumA[i+1] -= xv[i+1][0]
    if sumB[i+1] < C - xv[N-i][0]: sumB[i+1] = 0
    else: sumB[i+1] -= C - xv[N-i][0]

    maxA[i + 1] = maxA[i]
    if sumA[i+1] > maxA[i]:
        maxA[i+1] = sumA[i+1]
    maxB[i + 1] = maxB[i]
    if sumB[i+1] > maxB[i]:
        maxB[i+1] = sumB[i+1]

ans = 0
for i in range(N):
    #when to turn back?
    #valB = -xv[i][0] + max(sumB[:N-i+1])
    valB = -xv[i][0] + maxB[N - i]
    if valB < 0:
        ans = max(ans, sumA[i])
    else:
        ans = max(ans, sumA[i] + valB)

    #when to turn back?
    valA = -C+xv[N-i+1][0] + maxA[N-i]
    if valA < 0:
        ans = max(ans, sumB[i])
    else:
        ans = max(ans, sumB[i] + valA)

print((int(ans)))