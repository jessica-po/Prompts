N = int(input())
grid = []
x1 = 50
y1 = 50
x2 = -1
y2 = -1
for y in range(N):
    grid.append(list(map(int, input())))
    for x, num in enumerate(grid[-1]):
        if num == 4:
            x1 = min(x1, x)
            y1 = min(y1, y)
            x2 = max(x2, x)
            y2 = max(y2, y)

if x1 == 51:
    print('No')
else:
    for y in range(N):
        for x in range(N):
            ex = 0
            if x1 <= x <= x2 and y1 <= y <= y2:
                ex = 4
            elif (x == x1-1 or x == x2+1) and y1 <= y <= y2:
                ex = 2
            elif (y == y1-1 or y == y2+1) and x1 <= x <= x2:
                ex = 2
            elif (x == x1-1 or x == x2+1) and (y == y1-1 or y == y2+1):
                ex = 1
            if ex != grid[y][x]:
                print('No')
                break
        else:
            continue
        break
    else:
        print('Yes')