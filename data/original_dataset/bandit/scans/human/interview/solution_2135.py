h, w = list(map(int, input().split()))
field = [[c == "." for c in input()] + [False] for i in range(h)]
field.append([False] * (w + 1))

subVerts = [[0] * (w + 1) for i in range(h + 1)]
subHoriz = [[0] * (w + 1) for i in range(h + 1)]

for y in range(h):
    subVerts[y][0] = 0
    subHoriz[y][0] = 0

for x in range(w):
    subHoriz[0][x] = 0
    subVerts[0][x] = 0

for y in range(h):
    for x in range(w):
        subVerts[y + 1][x + 1] = subVerts[y + 1][x] + subVerts[y][x + 1] - subVerts[y][x]
        if field[y][x] and field[y - 1][x]:
            subVerts[y + 1][x + 1] += 1
        
        subHoriz[y + 1][x + 1] = subHoriz[y + 1][x] + subHoriz[y][x + 1] - subHoriz[y][x]
        if field[y][x] and field[y][x - 1]:
            subHoriz[y + 1][x + 1] += 1



q = int(input())
for i in range(q):
    y1, x1, y2, x2 = [int(x) - 1 for x in input().split()]
    ansHoriz = subHoriz[y2 + 1][x2 + 1] - subHoriz[y1][x2 + 1] - subHoriz[y2 + 1][x1 + 1] + subHoriz[y1][x1 + 1]
    ansVerts = subVerts[y2 + 1][x2 + 1] - subVerts[y1 + 1][x2 + 1] - subVerts[y2 + 1][x1] + subVerts[y1 + 1][x1]
    print(ansHoriz + ansVerts)