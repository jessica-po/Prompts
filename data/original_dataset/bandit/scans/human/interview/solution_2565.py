for _ in range(int(input())):
    a,b,c = list(map(int, input().split()))
    x,y,z = list(map(int, input().split()))

    temp = min(c,y)
    ans = 2*temp
    c -= temp
    y -= temp
    temp = min(c,z)
    c -= temp
    z -= temp
    temp = min(c,x)
    c -= temp
    x -= temp

    temp = min(a,z)
    a -= temp
    z -= temp
    temp = min(b,z)
    ans -= 2*temp
    b -= temp
    z -= temp
    print(ans)