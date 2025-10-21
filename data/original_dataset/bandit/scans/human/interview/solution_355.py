grid = [list(input()) for i in range(8)]
b = 9
w = 9
tblock = False
bblock = False
for r in range(8):
    for c in range(8):
        for ri in range(r):
            if grid[ri][c] == 'B':
                tblock = True
        for ri in range(r+1, 8):
            if grid[ri][c] == 'W':
                bblock = True
        if grid[r][c] == 'B' and not bblock:
            b = min([abs(7-r), b])
        elif grid[r][c] == 'W' and not tblock:
            w = min([w, r])
        tblock = False
        bblock = False
if b < w:
    print('B')
else:
    print('A')