def main():
    n = int(input())
    l = list(map(int, input().split()))
    seive = [False, True] * max(l)
    a = len(seive)
    for i in range(3, int(a ** .5) + 1, 2):
        if seive[i]:
            for j in range(i * i, a, i):
                seive[j] = False
    i = l.count(1)
    if i:
        res = [1] * i
        for a in l:
            if a > 1 and seive[a + 1]:
                res.append(a)
                break
        if len(res) > 1:
            print(len(res))
            print(*res)
            return
    l0, l1 = [], []
    for a in l:
        if a != 1:
            if a & 1:
                for b in l0:
                    if seive[a + b]:
                        print(2)
                        print(a, b)
                        return
                l1.append(a)
            else:
                for b in l1:
                    if seive[a + b]:
                        print(2)
                        print(a, b)
                        return
                l0.append(a)
    print(1)
    print(l[0])


def __starting_point():
    main()

__starting_point()