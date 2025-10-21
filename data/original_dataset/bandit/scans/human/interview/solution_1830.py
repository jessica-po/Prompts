n, m = map(int, input().split())
sum = n ** 2
colx = n
coly = n
usedx = [False] * n
usedy = [False] * n
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if not usedx[x]:
        sum -= coly
        usedx[x] = True
        colx -= 1
    if not usedy[y]:
        sum -= colx
        usedy[y] = True
        coly -= 1
    print(sum, end = ' ')