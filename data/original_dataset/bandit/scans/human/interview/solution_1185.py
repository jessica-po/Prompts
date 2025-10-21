from itertools import accumulate


def main():
    n, m, k = list(map(int, input().split()))
    
    a = list(map(int, input().split()))
    km = k * m
    
    if m == 1:
        a.sort(reverse=True)
        print(sum(a[:k]))
        return

    a = list(accumulate(a))
    a.append(0)

    if n == km:
        print(a[n-1])
        return

    d = [[0] * (n+1) for _ in range(k+1)]

    for i in range(m - 1, n):
        _k = (i + 1) // m if i < km else k
        for j in range(1, _k + 1):
            if i == j*m-1:
                d[j][i] = a[i]
            else:
                d[j][i] = max(d[j][i-1], a[i] - a[i-m] + d[j-1][i-m])

    print(d[k][n-1])


def __starting_point():
    main()


__starting_point()