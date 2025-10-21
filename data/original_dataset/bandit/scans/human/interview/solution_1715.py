from bisect import bisect_left

A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]

x = []
for s in S:
    idx = bisect_left(T, s)
    if idx == 0:
        x.append(abs(s-T[0]))
    elif idx == B:
        x.append(abs(s-T[-1]))
    else:
        x.append(min(abs(s-T[idx]), abs(s-T[idx-1])))

y = []
for t in T:
    idx = bisect_left(S, t)
    if idx == 0:
        y.append(abs(t-S[0]))
    elif idx == A:
        y.append(abs(t-S[-1]))
    else:
        y.append(min(abs(t-S[idx]), abs(t-S[idx-1])))

for _ in range(Q):
    X = int(input())

    sa = 0
    si = bisect_left(S, X)

    if si == 0:
        sa = x[0]+abs(S[0]-X)
    elif si == A:
        sa = x[-1]+abs(S[-1]-X)
    else:
        sa = min(x[si]+abs(S[si]-X), x[si-1]+abs(S[si-1]-X))

    ti = bisect_left(T, X)

    if ti == 0:
        ta = y[0]+abs(T[0]-X)
    elif ti == B:
        ta = y[-1]+abs(T[-1]-X)
    else:
        ta = min(y[ti]+abs(T[ti]-X), y[ti-1]+abs(T[ti-1]-X))
    
    print(min(sa, ta))