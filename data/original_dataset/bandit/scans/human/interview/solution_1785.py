def main():
    n = int(input())
    l = [0] * 85
    for c in input():
        l[ord(c)] += 1
    a, c, g, t = sorted(l[_] for _ in (65, 67, 71, 84))
    if g < t:
        print(1)
    elif c < g:
        print(pow(2, n, 1000000007))
    elif a < c:
        print(pow(3, n, 1000000007))
    else:
        print(pow(4, n, 1000000007))


def __starting_point():
    main()

__starting_point()