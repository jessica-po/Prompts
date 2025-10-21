def main():
    p = []
    sum_cost = 0
    n = int(input())
    for i in range(n):
        p.append(int(input()))
    max_p = max(p)
    p[p.index(max_p)] = max_p / 2
    print((int(sum(p))))


def __starting_point():
    main()

__starting_point()