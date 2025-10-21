h,w = map(int,input().split())
s = [list(input()) for i in range(h)]
hh = -1
tmp = -1
for k,i in enumerate(s):
    a = i.count('*')
    if tmp < a:
        tmp = a
        hh = k

t = [list(i) for i in list(zip(*s))]
ww = -1
tmp = -1
for k,i in enumerate(t):
    a = i.count('*')
    if tmp < a:
        tmp = a
        ww = k

if s[hh][ww] != '*':
    print('NO')
    return

if hh in (0, h - 1) or ww in (0, w - 1):
    print('NO')
    return

if '.' in (s[hh-1][ww], s[hh+1][ww], s[hh][ww-1], s[hh][ww+1]):
    print('NO')
    return

cnt = 1
for i in range(hh - 1, -1, -1):
    if s[i][ww] == '.':
        break
    cnt += 1
for i in range(ww - 1, -1, -1):
    if s[hh][i] == '.':
        break
    cnt += 1
for i in range(hh + 1, h):
    if s[i][ww] == '.':
        break
    cnt += 1
for i in range(ww + 1, w):
    if s[hh][i] == '.':
        break
    cnt += 1

for i in range(h):
    for j in range(w):
        cnt -= (s[i][j] == '*')

if cnt != 0:
    print('NO')
else:
    print('YES')