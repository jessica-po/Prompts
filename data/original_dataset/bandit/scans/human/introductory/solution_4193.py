a = list(list(map(int,input().split())) for _ in range(3))
n = int(input())
b = list(int(input()) for _ in range(n))

for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            a[i][j] = 0

for i in range(3):
    if a[i][0] == a[i][1] == a[i][2] or a[0][i] == a[1][i] == a[2][i] or a[0][0] == a[1][1] == a[2][2] or a[2][0] == a[1][1] == a[0][2]:
        print("Yes")
        break
else:
     print("No")