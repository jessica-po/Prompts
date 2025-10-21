t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    grid = [list(input()) for _ in range(n)]

    has_good = any('G' in l for l in grid)

    if not has_good:
        print("Yes")
        continue

    impossible = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 'B':
                continue

            for nbi, nbj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= nbi < n and 0 <= nbj < m:
                    if grid[nbi][nbj] == 'G':
                        impossible = True
                        break
                    elif grid[nbi][nbj] == 'B' or grid[nbi][nbj] == '#':
                        continue
                    elif grid[nbi][nbj] == '.':
                        grid[nbi][nbj] = "#"
                    else:
                        assert False, "What's in the grid?"

    if grid[n-1][m-1] == '#' or impossible:
        print("No")
        continue

    seen = [[False]*m for _ in range(n)]
    stack = [(n-1, m-1)]
    seen[n-1][m-1] = True

    while len(stack):
        i, j = stack.pop()

        for nbi, nbj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= nbi < n and 0 <= nbj < m:
                if grid[nbi][nbj] != '#' and not seen[nbi][nbj]:
                    seen[nbi][nbj] = True
                    stack.append((nbi, nbj))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G' and not seen[i][j]:
                impossible = True
                break
        if impossible:
            break

    if impossible:
        print("No")
    else:
        print("Yes")