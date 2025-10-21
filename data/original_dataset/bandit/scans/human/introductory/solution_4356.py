n, m = map(int, input().split())
a = ["" for _ in range(n)]
b = ["" for _ in range(m)]
for i in range(n):
    a[i] = str(input())
for i in range(m):
    b[i] = str(input())
def check(ini_x, ini_y):
    nonlocal n, m, a, b
    for x in range(m):
        for y in range(m):
            if a[ini_x + x][ini_y + y] != b[x][y]:
                return False
    return True
for i in range(n - m + 1):
    for j in range(n - m + 1):
        if check(i, j):
            print("Yes")
            return
print("No")