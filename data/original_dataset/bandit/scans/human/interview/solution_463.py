n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [0] * 1000000
ans = 0
go = False

for i in a:
    b[i] += 1
    if b[i] > 1:
        go = True

if go:
    print(ans)
else:
    for i in a:
        b[i] -= 1
        if b[i & x] + 1 > 1:
            go = True
            ans = 1
            break
        
        b[i] += 1
    
    if go:
        print(ans)
    else:
        c = [i & x for i in a]
        b = [0] * 1000000
        for i in c:
            b[i] += 1
            if (b[i] > 1):
                ans = 2
                go = True
                break
        if go:
            print(ans)
        else:
            print(-1)