for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n//2):
        for j in range(m//2):
            a = [arr[i][j], arr[n-i-1][j], arr[i][m-j-1], arr[n-i-1][m-j-1]]
            a.sort()
            res += (a[1]-a[0]) + (a[2]-a[1]) + (a[3]-a[1])
    if n%2 == 1:
        i = n//2
        for j in range(m//2):
            res += abs(arr[i][j] - arr[i][m-j-1])
    if m%2 == 1:
        j = m//2
        for i in range(n//2):
            res += abs(arr[i][j] - arr[n-i-1][j])
    print(res)