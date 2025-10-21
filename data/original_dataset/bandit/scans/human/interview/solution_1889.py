def cons(l):
    m = 0
    res = 0
    for v in l:
        if v:
            res += 1
            if res > m:
                m = res
        else:
            res = 0
    return m

n, m, q = list(map(int, input().split()))
grid = []
curr = [0] * n
for i in range(n):
    grid.append(list(map(int, input().split())))
    curr[i] = cons(grid[i])

for _ in range(q):
    i, j = list(map(int, input().split()))
    i -= 1
    j -= 1
    grid[i][j] = 0 if grid[i][j] else 1
    curr[i] = cons(grid[i])
    print(max(curr))