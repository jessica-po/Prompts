n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))
k = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == '#':
            if i+2<=n-1 and j-1>=0 and j+1<=n-1:
                if arr[i+1][j-1] == '#' and arr[i+1][j] == '#' and arr[i+1][j+1] == '#' and arr[i+2][j] == '#':
                    arr[i+1][j-1] = '.'
                    arr[i+1][j] = '.'
                    arr[i+1][j+1] = '.'
                    arr[i+2][j] = '.'
                    arr[i][j] = '.'
                else:
                    k = 0
                    break
            else:
                k = 0
                break
if k == 1:
    print('YES')
else:
    print('NO')