import itertools

unfold = itertools.chain.from_iterable

speedup = 400000

def jumps(a):
    d = speedup
    while d < a - 1:
        c = (a + d - 1) // d
        d = (a + c - 2) // (c - 1)
        yield d


def calc(d):
    return sum(d - 1 - (i - 1) % d for i in a)

def ans():
    for d, pd in zip(D, D[1:]):
        d -= 1
        cd = calc(d)
        if cd <= k:
            return d
        if d == pd:
            continue
        cpd = calc(pd)
        if d - pd >= (cd - k) * (d - pd) / (cd - cpd):
            return d - (cd - k) * (d - pd) / (cd - cpd)
    return 1

n, k = map(int, input().split())
a = list(map(int, input().split()))
speedup = min(speedup, 2 * int(max(a) ** 0.5))

D = sorted(set(range(1, speedup + 1)).union([max(a) + k + 1]).union(set(
    unfold(map(jumps, a)))), reverse=True)
    
print('%d' % ans())