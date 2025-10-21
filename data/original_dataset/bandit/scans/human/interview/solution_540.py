def read_data():
    n, m = map(int, input().split())
    maze = [[False] * (m + 2)]
    for i in range(n):
        maze.append([False] + [c == '.' for c in input().rstrip()] + [False])
    maze.append([False] * (m + 2))
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    return n, m, maze, r1, c1, r2, c2


def solve(n, m, maze, r1, c1, r2, c2):
    dots = count_surrounding_intact_ices(maze, r2, c2)
    if maze[r2][c2] == False:
        if r1 == r2 and c1 == c2:
            return dots >= 1
        else:
            return solve_wfs(n, m, maze, r1, c1, r2, c2)
    else:
        if dots >= 2:
            return solve_wfs(n, m, maze, r1, c1, r2, c2)
        if dots == 0:
            return False
        if dots == 1:
            return is_side_by_side(r1, c1, r2, c2)


def is_side_by_side(r1, c1, r2, c2):
    if r1 == r2:
        return abs(c1 - c2) == 1
    if c1 == c2:
        return abs(r1 - r2) == 1
    return False


def count_surrounding_intact_ices(maze, r, c):
    count = 0
    for rr, cc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if maze[rr][cc]:
            count += 1
    return count

def solve_wfs(n, m, maze, r1, c1, r2, c2):
    frontier = [(r1, c1)]
    while frontier:
        new_frontier = []
        for r, c in frontier:
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if nr == r2 and nc == c2:
                    return True
                if not maze[nr][nc]:
                    continue
                maze[nr][nc] = False
                new_frontier.append((nr, nc))
        frontier = new_frontier
    return False

def __starting_point():
    n, m, maze, r1, c1, r2, c2 = read_data()
    if solve(n, m, maze, r1, c1, r2, c2):
        print('YES')
    else:
        print('NO')
__starting_point()