nmq = input().split(' ')
n, m, q = int(nmq[0]), int(nmq[1]), int(nmq[2])
mt = []
for i in range(0, n):
    mt.append([])
    for j in range(0, m):
        mt[-1].append((i, j))
res = []
for i in range(0, n):
    res.append([])
    for j in range(0, m):
        res[-1].append(0)
for i in range(0, q):
    ins = input().split(' ')
    if ins[0] == '1':
        r = int(ins[1]) - 1
        b = mt[r][0]
        for j in range(0, m-1):
            mt[r][j] = mt[r][j+1]
        mt[r][m-1] = b
    if ins[0] == '2':
        c = int(ins[1]) - 1
        b = mt[0][c]
        for j in range(0, n-1):
            mt[j][c] = mt[j+1][c]
        mt[n-1][c] = b
    if ins[0] == '3':
        r = int(ins[1]) - 1
        c = int(ins[2]) - 1
        x = int(ins[3])
        p = mt[r][c]
        res[p[0]][p[1]] = x
for i in range(0, n):
    for j in range(0, m-1):
        print(res[i][j],' ', end='')
    print(res[i][-1])