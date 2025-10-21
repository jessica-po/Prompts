a = [[None] * 9 for i in range(9)]

for k in range(3):
    for i in range(3):
        sl = input().split()
        for j in range(3):
            for l in range(3):
                a[k * 3 + i][j * 3 + l] = sl[j][l]
    if k != 2:
        tmp = input()

x, y = map(int, input().split())
x -= 1
y -= 1

bx = x % 3
by = y % 3

ok = False
for i in range(bx * 3, bx * 3 + 3):
    for j in range(by * 3, by * 3 + 3):
        if a[i][j] == '.':
            ok = True
            a[i][j] = '!'
if not ok:
    for i in range(9):
        for j in range(9):
            if a[i][j] == '.':
                a[i][j] = '!'

for k in range(3):
    for i in range(3):
        for j in range(3):
            for l in range(3):
                print(a[k * 3 + i][j * 3 + l], end="")
            print(" ", end="")
        print()
    print()