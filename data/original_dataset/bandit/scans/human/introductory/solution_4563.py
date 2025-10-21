import sys
readline = sys.stdin.readline
def ceil(a, b):
    return -(-a//b)

def main():
    N = int(readline())
    inp = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]
    scr_t, scr_a = 0, 0
    for t, a in inp:
        if t >= scr_t and a >= scr_a:
            scr_t = t
            scr_a = a
        elif t < scr_t and a >= scr_a:
            scr_t = t * ceil(scr_t, t)
            scr_a = scr_t * a // t
        elif a < scr_a and t >= scr_t:
            scr_a = a * ceil(scr_a, a)
            scr_t = scr_a * t // a
        else:
            if t / a >= scr_t / scr_a:
                scr_a = a * ceil(scr_a, a)
                scr_t = scr_a * t // a
            else:
                scr_t = t * ceil(scr_t, t)
                scr_a = scr_t * a // t

    print((scr_t + scr_a))

def __starting_point():
    main()

__starting_point()