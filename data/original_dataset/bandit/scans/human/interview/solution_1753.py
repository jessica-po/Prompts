n, m = list(map(int, input().split()))
color_pairs = [list(map(int, input().split())) for i in range(m)]
towers = [[(i, i)] for i in range(1, n + 1)]
last_coord = n + 1
for c1, c2 in color_pairs:
    towers[c1 - 1].append((last_coord, c1))
    towers[c2 - 1].append((last_coord, c2))
    last_coord += 1
for i in range(len(towers)):
    print(len(towers[i]))
    for x, y in towers[i]:
        print(x, y)