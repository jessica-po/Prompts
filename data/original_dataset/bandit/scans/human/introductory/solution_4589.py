# 愚直
h, w = map(int, input().split())
table = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if table[i][j] == ".":
            num = 0
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if 0 <= i + y < h and 0 <= j + x < w:
                        if table[i + y][j + x] == "#":
                            num += 1
            table[i][j] = str(num)
for t in table:
    print("".join(t))