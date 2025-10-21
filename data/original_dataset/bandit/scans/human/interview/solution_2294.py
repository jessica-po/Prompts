from bisect import *
d = [{}, {}]
i = [0, 0]
for q in range(int(input())):
    a, t, x = map(int, input().split())
    for k in [0, 1]:
        d[k][x] = d[k].get(x, [])
        i[k] = bisect(d[k][x], t)
    if a < 3: d[-a][x].insert(i[-a], t)
    else: print(i[1] - i[0])