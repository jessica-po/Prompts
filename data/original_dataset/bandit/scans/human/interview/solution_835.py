def main():
    s = input()
    a = b = c = 0
    for elem in s:
        if elem == "B":
            a += 1
        elif elem == "S":
            b += 1
        else:
            c += 1
    na, nb, nc = map(int, input().split())
    pa, pb, pc = map(int, input().split())
    k = int(input())

    l = 0
    r = 10**13
    while r - l > 1:
        m = (l + r) // 2
        cntA = max(0, a * m - na)
        cntB = max(0, b * m - nb)
        cntC = max(0, c * m - nc)
        money = cntA * pa + cntB * pb + cntC * pc
        if money <= k:
            l = m
        else:
            r = m
    print(l)

main()