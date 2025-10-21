a, b = list(map(int,input().split()))
if a <= b:
    l = 0
    r = a + 1
    while r - l > 1:
        m = (l + r) // 2
        if m * (m + 1) // 2 > a:
            r = m
        else:
            l = m
    n = l
    a -= n*(n+1) // 2
    c = 1
    N = [i + 1 for i in range(n)]    
    if a > 0:
        c = n + 1 - a
        N.pop(c - 1)
        N.append(c + a)
        N[-1] = c + a
    D = []
    if a != 0:
        b -= c
        D = [c]
        n = n + 1
    n += 1
    while b >= 0:
        b -= n
        D.append(n)
        n += 1
    D.pop(-1)
    print(len(N))
    if len(N) != 0:
        print(*N)
    print(len(D))
    if len(D) != 0:
        print(*D)
else:
    c = a
    a = b
    b = c
    l = 0
    r = a + 1
    while r - l > 1:
        m = (l + r) // 2
        if m * (m + 1) // 2 > a:
            r = m
        else:
            l = m
    n = l
    a -= n*(n+1) // 2
    c = 1
    N = [i + 1 for i in range(n)]    
    if a > 0:
        c = n + 1 - a
        N.pop(c - 1)
        N.append(c + a)
        N[-1] = c + a
    D = []
    if a != 0:
        b -= c
        D = [c]
        n = n + 1
    n += 1
    while b >= 0:
        b -= n
        D.append(n)
        n += 1
    D.pop(-1)
    print(len(D))
    if len(D) != 0:
        print(*D)
    print(len(N))
    if len(N) != 0:
        print(*N)