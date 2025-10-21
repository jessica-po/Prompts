N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

odd = []
for (x, y) in P:
    dist = abs(x) + abs(y)
    odd.append(dist % 2 != 0)

valid = True
even = False
if all(odd):
    pass
elif not any(odd):
    even = True
else:
    valid =False

if valid:

    M = 31
    if even:
        print((M+1))
        print((*([1 << m for m in range(M)] + [1])))
    else:
        print(M)
        print((*[1 << m for m in range(M)]))

    for (x, y) in P:
        u = x + y
        v = x - y
        if even:
            u += 1
            v += 1
        if u >= 0 and v >= 0:
            A = 'R'
            B = 'U'
            C = 'D'
            D = 'L'
        elif u >= 0 and v < 0:
            v *= -1
            A = 'U'
            B = 'R'
            C = 'L'
            D = 'D'
        elif u < 0 and v >= 0:
            u *= -1
            A = 'D'
            B = 'L'
            C = 'R'
            D = 'U'
        elif u < 0 and v < 0:
            u *= -1
            v *= -1
            A = 'L'
            B = 'D'
            C = 'U'
            D = 'R'

        ans = ''
        wa = ((1 << M) - 1 - u) // 2
        sa = ((1 << M) - 1 - v) // 2
        for i in range(M):
            check = str(wa >> i & 1) + str(sa >> i & 1)
            if check == '00':
                ans += A
            elif check == '01':
                ans += B
            elif check == '10':
                ans += C
            elif check == '11':
                ans += D
        if even:
            ans += 'L'
        print(ans)
else:
    print((-1))