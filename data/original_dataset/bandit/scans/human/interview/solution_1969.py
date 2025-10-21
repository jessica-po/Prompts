n = int(input())

a = [input() for i in range(n)]

ans = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if a[i][j] == 'X' and a[i + 1][j + 1] == 'X' and a[i - 1][j + 1] == 'X' and a[i + 1][j - 1] == 'X' and a[i - 1][j - 1] == 'X':
            ans += 1
            
print(ans)