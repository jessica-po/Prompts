a = int(input())
for i in range(a):
    a1, b, c, n = list(map(int, input().split()))
    t = max(a1, b, c)
    if ((a1 + b + c + n) % 3 == 0 and t <= (a1 + b + c + n)//3 ):
        print('YES')
    else:
        print('NO')