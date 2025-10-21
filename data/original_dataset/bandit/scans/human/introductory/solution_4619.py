def main():
    w, h, n = list(map(int, input().split()))

    x_min = 0
    x_max = w
    y_min = 0
    y_max = h

    for _ in range(n):
        x, y, a = list(map(int, input().split()))
        if a == 1:
            x_min = max(x_min, x)
        elif a == 2:
            x_max = min(x_max, x)
        elif a == 3:
            y_min = max(y_min, y)
        else:
            y_max = min(y_max, y)

    print((
        (x_max - x_min) * (y_max - y_min)
        if x_min < x_max and y_min < y_max else 0
    ))


def __starting_point():
    main()

__starting_point()