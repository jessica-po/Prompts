def main():
    s, x, pfx = input(), 0, []
    a, b = list(map(int, input().split()))
    try:
        for i, c in enumerate(s, 1):
            x = (x * 10 + ord(c) - 48) % a
            if not x and s[i] != '0':
                pfx.append(i)
    except IndexError:
        pass
    x, p, i = 0, 1, len(s)
    for stop in reversed(pfx):
        for i in range(i - 1, stop - 1, -1):
            x = (x + (ord(s[i]) - 48) * p) % b
            p = p * 10 % b
        if not x:
            print("YES")
            print(s[:i])
            print(s[i:])
            return
    print("NO")


def __starting_point():
    main()

__starting_point()