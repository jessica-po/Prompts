import bisect

n,m = map(int,input().split())

Q = []
P = [[] for _ in range(n)]
for i in range(m):
    p,y = map(int,input().split())
    Q.append([p,y])
    P[p-1].append(y)

P_1 = [sorted(l) for l in P]

for p,y in Q:
    a = str(p).zfill(6)
    b = str(bisect.bisect(P_1[p-1], y)).zfill(6)
    print(a+b)