n, m = map(int, input().split())
pole = []
metka = []
for i in range(n):
    pole.append([])
    metka.append([])
    s = input()
    for j in range(m):
        pole[i].append(s[j])
        if s[j] == '.':
            metka[i].append(0)
        else:
            metka[i].append(1)
k = 0
ans = []

for i in range(n):
    for j in range(m):
        if pole[i][j] == '*':
            e = 0
            while i - e - 1>= 0 and j - e - 1>= 0 and i + e + 1 < n and j + e + 1< m and pole[i - e - 1][j] == '*' and pole[i][j - e - 1] == '*' and pole[i + e + 1][j] == '*' and pole[i][j + e + 1] == '*':
                e = e + 1
                metka[i][j] = 0
                metka[i - e][j] = 0
                metka[i][j - e] = 0
                metka[i + e][j] = 0
                metka[i][j + e] = 0
            if e != 0:
                k = k + 1
                ans.append((i + 1,j + 1, e))
flag = True
for i in range(n):
    if 1 in metka[i]:
        flag = False
        break
if not flag:
    print(-1)
else:
    print(k)
    for i in range(k):
        print(ans[i][0], ans[i][1], ans[i][2], end='\n')