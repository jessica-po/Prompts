from collections import defaultdict
import bisect

n = int(input())
x0, y0 = list(map(int, input().split(' ')))
verticale = []
horizontale = []
diagonale1 = []
diagonale2 = []
for _ in range(n):
    t, x, y = input().split(' ')
    x, y = int(x), int(y)
    if x == x0:
        verticale.append((y, t))
    if y == y0:
        horizontale.append((x, t))
    if x+y == x0+y0:
        diagonale1.append((x, t))
    if x-y == x0-y0:
        diagonale2.append((x, t))

dead = False
v = sorted(verticale)
if v:
    l = bisect.bisect(v, (y0, 'K'))
    if 0 < l < len(v):
        if v[l][1] in {'Q', 'R'} or v[l-1][1] in {'Q', 'R'}:
            dead = True
    elif l == 0:
        if v[0][1] in {'Q', 'R'}:
            dead = True
    else:
        if v[len(v)-1][1] in {'Q', 'R'}:
            dead = True
v = sorted(horizontale)
if v:
    l = bisect.bisect(v, (x0, 'K'))
    if 0 < l < len(v):
        if v[l][1] in {'Q', 'R'} or v[l-1][1] in {'Q', 'R'}:
            dead = True
    elif l == 0:
        if v[0][1] in {'Q', 'R'}:
            dead = True
    else:
        if v[len(v)-1][1] in {'Q', 'R'}:
            dead = True
v = sorted(diagonale1)
if v:
    l = bisect.bisect(v, (x0, 'K'))
    if 0 < l < len(v):
        if v[l][1] in {'Q', 'B'} or v[l-1][1] in {'Q', 'B'}:
            dead = True
    elif l == 0:
        if v[0][1] in {'Q', 'B'}:
            dead = True
    else:
        if v[len(v)-1][1] in {'Q', 'B'}:
            dead = True
v = sorted(diagonale2)
if v:
    l = bisect.bisect(v, (x0, 'K'))
    if 0 < l < len(v):
        if v[l][1] in {'Q', 'B'} or v[l-1][1] in {'Q', 'B'}:
            dead = True
    elif l == 0:
        if v[0][1] in {'Q', 'B'}:
            dead = True
    else:
        if v[len(v)-1][1] in {'Q', 'B'}:
            dead = True
if dead:
    print('YES')
else:
    print('NO')