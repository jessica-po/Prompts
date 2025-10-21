h,w = map(int, input().split())
cell = []

for i in range(h):
    row = list(input())
    if row != ["."]*w:
        cell.append(row)

counter = []
for i in range(w):
    flag = 0
    for j in range(len(cell)):
        if cell[j][i] == "#":
            flag = 1
            break
    if flag == 1:
            counter.append(i)

for a in cell:
    ans = ''
    for i in counter:
        ans = ans + a[i]
    print(ans)