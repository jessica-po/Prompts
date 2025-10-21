from bisect import bisect_right


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.reverse()
    lis = [a[0]]
    for i in range(1, n):
        if a[i] >= lis[-1]:
            lis.append(a[i])
        else:
            lis[bisect_right(lis, a[i])] = a[i]
    print((len(lis)))


def __starting_point():
    main()

__starting_point()