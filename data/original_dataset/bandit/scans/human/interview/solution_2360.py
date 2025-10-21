t = int(input())

for _ in range(t):
    n = int(input())
    lims = [tuple(int(v) for v in input().split()) for _ in range(n)]
    ctime = 0
    ans = []
    for l, r in lims:
        if l >= ctime:
            ans.append(l)
            ctime = l + 1
        elif r < ctime:
            ans.append(0)
        else:
            ans.append(ctime)
            ctime += 1
    print(' '.join(str(v) for v in ans))