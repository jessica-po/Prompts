t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    for i in range(60, -1, -1):
        m = k ** i
        for j in range(n):
            if a[j] >= m:
                a[j] -= m
                break
    if all(i == 0 for i in a):
        print('YES')
    else:
        print('NO')