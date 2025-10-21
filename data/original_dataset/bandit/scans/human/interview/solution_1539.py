from collections import defaultdict


def main():
    n = int(input())
    hh = list(map(int, input().split()))
    ee = list(map(int, input().split()))
    dd = defaultdict(set)
    for i, h in enumerate(hh):
        dd[h].add(i)
    idx = sorted(list(range(n)), key=ee.__getitem__, reverse=True)
    res = 0
    for h, s in list(dd.items()):
        x = sum(ee[i] for i in s)
        le = len(s) - 1
        if le:
            for i in idx:
                if hh[i] < h and i not in s:
                    x += ee[i]
                    le -= 1
                    if not le:
                        break
        if res < x:
            res = x
    print(sum(ee) - res)


def __starting_point():
    main()

__starting_point()