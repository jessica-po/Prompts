n = int(input())
s = []
for i in range(n):
    s.append(input())
new = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j] == 'o':
            new[i][j] = 1
flag = True
for i in range(n):
    for j in range(n):
        s = 0
        if i > 0 and new[i - 1][j] == 1:
            s += 1
        if i < n - 1 and new[i + 1][j] == 1:
            s += 1
        if j > 0 and new[i][j - 1] == 1:
            s += 1
        if j < n - 1 and new[i][j + 1] == 1:
            s += 1
        if s % 2 == 1:
            flag = False
            break
if flag:
    print("YES")
else:
    print("NO")