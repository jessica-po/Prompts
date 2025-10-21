def main():
    N, *A = list(map(int, open(0).read().split()))

    B = sorted(A)
    l, r = 0, N
    m, c = N // 2, N * (N + 1) // 2

    def check(x):
        b, r, y = N, 0, 0
        D = [0] * (2 * N + 1)
        for a in A:
            D[b] += 1
            if a < x:
                r += D[b]
                b += 1
            else:
                b -= 1
                r -= D[b]
            y += r
        return y

    while True:
        if check(B[m]) <= c // 2:
            if m == N - 1 or check(B[m + 1]) > c // 2:
                break
            l, m = m, (m + r) // 2
        else:
            m, r = (m + l) // 2, m + 1

    print((B[m]))


def __starting_point():
    main()

__starting_point()