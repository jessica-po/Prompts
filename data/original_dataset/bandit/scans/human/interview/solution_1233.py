arr = [0 for i in range(5001)]


def insertion_sort(n, a):
    def modify(t):
        while t > 0:
            arr[t] += 1
            t -= t & (-t)

    def query(t):
        res = 0
        while t < 5001:
            res += arr[t]
            t += t & (-t)
        return res

    s = 0
    ans = 0
    way = 0

    for i in range(n):
        a[i] += 1

    for i in range(n):
        nonlocal arr
        arr = [0 for j in range(5001)]
        for j in range(i + 1, n):
            if a[i] < a[j]:
                continue
            s += 1
            tmp = 1 + 2 * query(a[j])
            if tmp > ans:
                ans = tmp
                way = 1
            elif tmp == ans:
                way += 1
            modify(a[j])

    return s - ans, way


def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))
    result = insertion_sort(n, a)
    print(*result)

__starting_point()