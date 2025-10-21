N = int(input())
table = []
for i in range(N):
    table.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            continue
        flg = False
        for s in range(N):
            for t in range(N):
                if table[i][j] == table[i][s] + table[t][j]:
                    flg = True
                    break
        if not flg:
            print("No")
            return
print("Yes")