def main():
    a = list(input())
    b = list(input())

    n = len(a)
    k = n
    while k % 2 == 0:
        k = k // 2

    while k != n:
        pairs = n // (k * 2)
        for i in range(0, pairs * 2, 2):
            if a[k * i:k * (i + 1)] > a[k * (i + 1):k * (i + 2)]:
                a[k * i:k * (i + 1)], a[k * (i + 1):k * (i + 2)] = a[k * (i + 1):k * (i + 2)], a[k * i:k * (i + 1)]
            if b[k * i:k * (i + 1)] > b[k * (i + 1):k * (i + 2)]:
                b[k * i:k * (i + 1)], b[k * (i + 1):k * (i + 2)] = b[k * (i + 1):k * (i + 2)], b[k * i:k * (i + 1)]
        k *= 2

    if a == b:
        print('YES')
    else:
        print('NO')


main()