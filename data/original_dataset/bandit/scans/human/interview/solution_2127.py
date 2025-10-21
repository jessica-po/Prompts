import sys

n = int(sys.stdin.readline().strip())
m = 0
M = 0

for i in range (0, n):
    line = sys.stdin.readline().strip().split()
    s = line[0]
    x = min([int(line[1]), int(line[2])])
    y = max([int(line[1]), int(line[2])])
    if s == '+':
        m = max([m, x])
        M = max([M, y])
    else:
        if x >= m and y >= M:
            print("YES")
        else:
            print("NO")