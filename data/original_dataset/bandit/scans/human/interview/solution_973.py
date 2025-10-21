r, c = list(map(int, input().split()))
ls = [[c for c in input()] for i in range(r)]
for i in range(r):
    dead = False
    for j in range(c):
        if ls[i][j] == 'W':
            if i != 0 and ls[i - 1][j] == 'S': dead = True
            if i != r - 1 and ls[i + 1][j] == 'S': dead = True
            if j != 0 and ls[i][j - 1] == 'S': dead = True
            if j != c - 1 and ls[i][j + 1] == 'S': dead = True
            if dead: 
                break
        elif ls[i][j] == '.':
            ls[i][j] = 'D'
    if dead:
        print("No")
        break
else:
    print("Yes")
    for i in range(r):
        print(''.join(ls[i]))