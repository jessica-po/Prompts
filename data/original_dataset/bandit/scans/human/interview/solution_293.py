x = int(input())

def solve(x):
    count = 0
    lst = []
    x6 = x * 6
    for n in range(1, x + 1):
        t, r = divmod(x6, n*(n+1))
        if t < 2*n + 1:
            break
        if r:
            continue
        m, r = divmod(t + n - 1, 3)
        if r:
            continue
        count += 2
        lst.append((n, m))
    nn, mm = lst[-1]
    if nn == mm:
        count -= 1
    print(count)
    for n, m in lst:
        print(n, m)
    if nn != mm:
        print(mm, nn)
    lst.reverse()
    for n, m in lst[1:]:
        print(m, n)

solve(x)