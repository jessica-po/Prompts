t = int(input())
for yguagwu in range(t):
    n = int(input())
    a = sorted(list(map(int,input().split())))
    b = []
    for i in range(n):
        if i % 2 == 0:
            b.append(a[(-i//2-1)])
        else:
            b.append(a[i//2])
    print(*b[::-1])