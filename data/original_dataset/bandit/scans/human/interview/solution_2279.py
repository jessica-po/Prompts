n = int(input())

a = []
for i in range(2*n - 1):
    a.append([int(c) for c in input().split()])


c = []
for i in range(len(a)):
    for j in range(len(a[i])):
        c.append([a[i][j], i+1, j])

c.sort(reverse=True)
used = set()
res = [0]*2*n
for cc in c:
    if not cc[1] in used and not cc[2] in used:
        res[cc[1]] = cc[2] + 1
        res[cc[2]] = cc[1] + 1
        used.add(cc[1])
        used.add(cc[2])

print(' '.join(str(r) for r in res))