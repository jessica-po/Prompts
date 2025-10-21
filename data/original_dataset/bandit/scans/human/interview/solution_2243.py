n, k, q = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]
S = set()
for i in range(q):
    t, _id = [int(x) for x in input().split()]
    if t == 1:
        m = min(S, default = 0)
        if len(S) == k:
            if m < T[_id-1]:
                S.remove(m)
                S.add(T[_id-1])
        else:
            S.add(T[_id-1])
    else:
        print('YES' if T[_id-1] in S else 'NO')