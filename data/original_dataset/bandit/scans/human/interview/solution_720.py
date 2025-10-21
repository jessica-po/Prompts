def main():
    n = int(input())
    res = 0
    la, lb = 0, 0
    max_draw = -1
    for _ in range(n):
        a, b = [int(x) for x in input().split()]
        mx = max(la, lb)
        mn = min(a, b)
        if mx <= max_draw:
            mx = max_draw + 1
        if mx <= mn:
            res += mn - mx + 1
            max_draw = mn
        la, lb = a, b
    print(res)

def __starting_point():
    main()

__starting_point()