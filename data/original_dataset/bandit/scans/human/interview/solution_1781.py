n, k = list(map(int, input().split()))
plain = list()

for i in range(n):
    plain.append(list(input()))

fr = {
    "0": list(),
    "1": list(),
    "2": list(),
}
for i in range(n):
    for j in range(12):
        if plain[i][j] != ".":
            continue

        st = 0
        if j > 0 and plain[i][j - 1] == "S":
            st += 1
        if j < 11 and plain[i][j + 1] == "S":
            st += 1

        fr[str(st)].append((i, j))

for i in range(k):
    if len(fr["0"]):
        x, y = fr["0"].pop()
    elif len(fr["1"]):
        x, y = fr["1"].pop()
    else:
        x, y = fr["2"].pop()
    plain[x][y] = "x"


result = 0
for i in range(n):
    for j in range(12):
        if plain[i][j] != "S":
            continue
        if j > 0 and plain[i][j - 1] in ("S", "x", "P"):
            result += 1
        if j < 11 and plain[i][j + 1] in ("S", "x", "P"):
            result += 1

print(result)
for i in range(n):
    print("".join(plain[i]))