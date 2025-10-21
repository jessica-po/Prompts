def main():
    n, m, b, mod = list(map(int, input().split()))
    row_zero = [1] + [0] * b
    b += 1
    dp = [[0] * b for _ in range(m)]
    for a in list(map(int, input().split())):
        cur = row_zero
        for nxt in dp:
            for i, u in zip(list(range(a, b)), cur):
                nxt[i] = (nxt[i] + u) % mod
            cur = nxt
    print(sum(dp[-1]) % mod)


def __starting_point():
    main()

__starting_point()