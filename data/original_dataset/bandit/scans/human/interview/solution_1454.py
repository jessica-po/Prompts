n, m = map(int, input().split())
matr = [list(map(int, input().split())) for _ in range(n)]

for i, st in enumerate(matr):
    for j, elem in enumerate(st):
        if matr[~i][~j] == 0:
            matr[~i][~j] = min(matr[~i + 1][~j], matr[~i][~j + 1]) - 1

# print(*matr, sep='\n')

for i, st in enumerate(matr):
    for j, elem in enumerate(st):
        if i != 0 and j != 0:
            if matr[i][j] <= max(matr[i - 1][j], matr[i][j - 1]):
                print('-1')
                return
        elif i == 0 and j != 0:
            if matr[i][j] <= matr[i][j - 1]:
                print('-1')
                return
        elif i != 0 and j == 0:
            if matr[i][j] <= matr[i - 1][j]:
                print('-1')
                return
print(sum(sum(l) for l in matr))