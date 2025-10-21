for _ in range(int(input())):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    res = []
    if arr[n-2][n-1] == arr[n-1][n-2]:
        if arr[0][1] == arr[n-2][n-1]:
            res.append((1, 2))
        if arr[1][0] == arr[n-2][n-1]:
            res.append((2, 1))
    elif arr[0][1] == arr[1][0]:
        if arr[n-2][n-1] == arr[0][1]:
            res.append((n-1, n))
        if arr[n-1][n-2] == arr[0][1]:
            res.append((n, n-1))
    else:
        if arr[0][1] == "1":
            res.append((1, 2))
        if arr[1][0] == "1":
            res.append((2, 1))
        if arr[n-2][n-1] == "0":
            res.append((n-1, n))
        if arr[n-1][n-2] == "0":
            res.append((n, n-1))
    print(len(res))
    for e in res:
        print(*e)