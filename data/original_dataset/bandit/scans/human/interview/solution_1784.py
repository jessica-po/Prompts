n, k = map(int, input().split())
arr = [int(i) for i in input().split()]
res = [[] for i in range(n)]
c = 0
while True:
    z = 0
    for i in arr:
        if i > 0:
            z += 1
    if z == 0:
        break
    if z == n:
        for i in range(n):
            arr[i] -= 1
            res[i].append(1)
    else:
        c += 1
        if c > k:
            break
        for i, j in enumerate(arr):
            if j > 0:
                arr[i] -= 1
                res[i].append(c)
if c > k:
    print('NO')
else:
    print('YES')
    for i in res:
        for j in i:
            print(j, end = ' ')
        print()