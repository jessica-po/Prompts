import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
N = int(input())
C, Y = [], []
for _ in range(N):
    a, b, c = list(map(int, input().split()))
    C.append(a)
    Y.append(c - b)

if sum(Y):
    print(-1)
    return

X = [[] for i in range(N)]
for i in range(N-1):
    x, y = list(map(int, input().split()))
    X[x-1].append(y-1)
    X[y-1].append(x-1)

P = [-1] * N
Q = deque([0])
R = []
while Q:
    i = deque.popleft(Q)
    R.append(i)
    for a in X[i]:
        if a != P[i]:
            P[a] = i
            X[a].remove(i)
            deque.append(Q, a)

for i in R[1:]:
    C[i] = min(C[i], C[P[i]])

ans = 0
for i in R[1:][::-1]:
    if Y[i] * Y[P[i]] < 0:
        ans += C[P[i]] * min(abs(Y[i]), abs(Y[P[i]]))
    Y[P[i]] += Y[i]

print(ans * 2)