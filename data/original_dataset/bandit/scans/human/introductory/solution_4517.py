import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = list(map(int, input().split()))
X = [[] for i in range(N)]
for i in range(N-1):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    X[x].append(y)
    X[y].append(x)

P = [-1] * N
DE = [0] * N

def EulerTour(n, X, i0 = 0):
    Q = [~i0, i0]
    ct = -1
    ET = []
    ET1 = [0] * n
    ET2 = [0] * n
    de = -1
    while Q:
        i = Q.pop()
        if i < 0:
            ET2[~i] = ct
            de -= 1
            continue
        if i >= 0:
            ET.append(i)
            ct += 1
            if ET1[i] == 0: ET1[i] = ct
            de += 1
            DE[i] = de
        for a in X[i][::-1]:
            if a != P[i]:
                P[a] = i
                for k in range(len(X[a])):
                    if X[a][k] == i:
                        del X[a][k]
                        break
                Q.append(~a)
                Q.append(a)
    return (ET, ET1, ET2)

ET, ET1, ET2 = EulerTour(N, X, 0)

for _ in range(M):
    A = [max(P[int(a) - 1], 0) for a in input().split()][1:]
    mad = -1
    for a in A:
        if DE[a] > mad:
            mad = DE[a]
            maa = a
    e = ET1[maa]
    for a in A:
        if not (ET1[a] <= e <= ET2[a]):
            print("NO")
            break
    else:
        print("YES")