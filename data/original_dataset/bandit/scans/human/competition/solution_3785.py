import sys

n, m, k = (int(x) for x in sys.stdin.readline().split(' '))
maze = []
for i in range(n):
    maze.append(list(sys.stdin.readline().strip()))

for y in range(n):
    for x in range(m):
        if maze[y][x] == '.':
            x0, y0 = x, y
            break
    else:
        continue
    break
else:
    print('no spare room')
    return

stack = []
stack.append((x0,y0))
while stack:
    x, y = stack[-1]

    if maze[y][x] == '.':
        maze[y][x] = '0'
        if x > 0 and maze[y][x-1] == '.':
            stack.append((x-1, y))
    elif maze[y][x] == '0':
        maze[y][x] = '1'
        if y < n-1 and maze[y+1][x] == '.':
            stack.append((x, y+1))
    elif maze[y][x] == '1':
        maze[y][x] = '2'
        if x < m-1 and maze[y][x+1] == '.':
            stack.append((x+1, y))
    elif maze[y][x] == '2':
        maze[y][x] = '3'
        if y > 0 and maze[y-1][x] == '.':
            stack.append((x, y-1))
    elif maze[y][x] == '3':
        if k > 0:
            maze[y][x] = 'X'
            k -= 1
        stack.pop()

for y in range(n):
    for x in range(m):
        maze[y][x] = '.' if maze[y][x] == '3' else maze[y][x]

print("\n".join(["".join(s) for s in maze]))