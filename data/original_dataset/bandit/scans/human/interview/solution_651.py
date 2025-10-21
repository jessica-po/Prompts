import itertools

def valid(grid, path, perm, start, goal):
    x, y = start
    n = len(grid)
    m = len(grid[0])
    for move in path:
        dx, dy = perm[int(move)]
        x += dx
        y += dy
        if (x, y) == goal:
            return True
        if not (0 <= x < n and 0 <= y < m) or grid[x][y] == '#':
            return False

    return False

def main():
    n, m = list(map(int, input().split()))
    grid = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                sx, sy = i, j
                grid[i][j] = '.'
            elif grid[i][j] == 'E':
                gx, gy = i, j
                grid[i][j] = '.'


    path = input()
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ans = 0
    for perm in itertools.permutations(moves):
        if valid(grid, path, perm, (sx, sy), (gx, gy)):
            ans += 1

    print(ans)

main()