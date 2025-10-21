def check(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def dfs1(x, y, T=0):
    nonlocal first, used
    if not(check(x, y)) or used[x][y]:
        return
    used[x][y] = True
    first.add((x, y, T))
    for pair in (2, 2), (2, -2), (-2, 2), (-2, -2):
        dfs1(x + pair[0], y + pair[1], 1 - T)

def dfs2(x, y, T=0):
    nonlocal second, used
    if not(check(x, y)) or used[x][y]:
        return
    used[x][y] = True
    second.add((x, y, T))
    for pair in (2, 2), (2, -2), (-2, 2), (-2, -2):
        dfs2(x + pair[0], y + pair[1], 1 - T)


t = int(input())
for i in range(t):
    if i > 0:
        kuzma = input()
    board = [input() for i in range(8)]
    FoundFirst = False
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                if not(FoundFirst):
                    First = (i, j)
                    FoundFirst = True
                else:
                    Second = (i, j)

    used = [[0 for i in range(8)] for j in range(8)]
    first = set()
    dfs1(First[0], First[1])
    used = [[0 for i in range(8)] for j in range(8)]
    second = set()
    dfs2(Second[0], Second[1])
    intersection = first & second
    IsOk = False
    for x, y, t in intersection:
        if board[x][y] != '#':
            print("YES")
            IsOk = True
            break
    if not(IsOk):
        print("NO")
    board = []