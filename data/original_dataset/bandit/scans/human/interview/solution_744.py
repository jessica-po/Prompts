n = int(input())
s = input()
si, sf = 0, 0
for i in range(1, n):
    if s[i] == 'S' and s[i - 1] != 'S':
        si += 1
    elif s[i] == 'F' and s[i - 1] != 'F':
        sf += 1
if sf > si:
    print('YES')
else:
    print('NO')