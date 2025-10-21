n, m, k = list(map(int, str.split(input())))
f = tuple([str.strip(input()) for _ in range(n)])

r = []
for x in range(m):

    cr = sum([f[y][x] == "U" for y in range(0, n, 2)])
    for cx in range(max(0, x + 1 - n), x):

        cr += f[x - cx][cx] == "R"

    for cx in range(x + 1, min(m, n + x)):

        cr += f[cx - x][cx] == "L"

    r.append(cr)

print(str.join(" ", list(map(str, r))))