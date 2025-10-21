from math import sin, cos, tan, atan, pi


def main():
    w, h, a = map(int, input().split())
    a = min(a, 180 - a) * pi / 180
    if h > w:
        h, w = w, h
    if h * (1 + cos(a)) < w * sin(a):
        res = h * h / sin(a)
    else:
        res = h * w - ((w - h * tan(a / 2)) ** 2 * tan(a) + (h - w * tan(a / 2)) ** 2 * tan(a)) / 4
    print('{:.9f}'.format(res))


def __starting_point():
    main()
__starting_point()