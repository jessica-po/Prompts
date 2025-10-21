r, c = list(map(int, input().split()))

b = [list(input()) for i in range(r)]
for y in range(r):
    for x in range(c):
        if b[y][x] == '.':
            b[y][x] = '0'

ok = True
for Y in range(r):
    for X in range(c):
        if not b[Y][X].isdigit():
            continue
        p = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                y = Y + dy
                x = X + dx
                if 0 <= y < r and 0 <= x < c:
                    p += b[y][x] == '*'
        if p != int(b[Y][X]):
            ok = False

print(["NO", "YES"][ok])