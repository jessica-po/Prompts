def sol():

    n = int(input())
    st = list(map(int, input().split(' ')))
    d = {}
    for x in range(n):
        d[x] = []

    st = [(st[i], i) for i in range(len(st))]
    st = sorted(st)

    for a0 in range(n - 1):
        u, v = map(int, input().split(' '))
        u, v = u - 1, v - 1
        d[u].append(v)
        d[v].append(u)

    hardest = []
    almost = []

    single_hardest = st[-1][0]

    for x in st[::-1]:
        if x[0] == single_hardest:
            hardest.append(x[1])
        elif x[0] == single_hardest-1:
            almost.append(x[1])
        else:
            break

    def inter(a, b):
        c = []
        for x in a:
            if x in b:
                c.append(x)
        return c

    lower_bound = single_hardest

    inte = d[hardest[0]]+[hardest[0]]
    for h in hardest[1:]:
        inte = inter(inte, d[h]+[h])

    if not inte:
        return (single_hardest+2)

    if len(hardest) > 1:
        return single_hardest+1

    # hardest is len 1
    if not almost:
        return single_hardest

    cand = st[-1][1]

    for h in almost:
        if h not in d[cand]:
            return single_hardest+1
    return single_hardest

print(sol())