# bを必要なだけ(strideの分)右にずらせばよい
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ai, bi = 0, 0
    stride = 0
    while ai < n and bi < n:
        ax, bx = a[ai], b[bi]
        if ax == bx:
            cnt = 2

            ai += 1
            while ai < n and a[ai] == ax:
                cnt += 1
                ai += 1

            bi_copy = bi
            bi += 1
            while bi < n and b[bi] == bx:
                cnt += 1
                bi += 1

            if cnt > n:
                print('No')
                return

            if stride < ai - bi_copy:
                stride = ai - bi_copy

        elif ax < bx:
            ai += 1
        else:
            bi += 1

    print('Yes')
    print(' '.join(map(str, b[n-stride:] + b[:n-stride])))

main()