#!/usr/local/bin/python3


import sys

DEBUG = '-d' in sys.argv


def debug(*args, **kwargs):
    if DEBUG:
        print(*args, file=sys.stderr, **kwargs)

    return None



def main():
    n = int(input())

    cnt = [0] * (n + 1)
    edge = []

    for i in range(0, n + 1):
        edge.append(set())

    for i in range(0, 2 * n):
        s, t = map(int, input().split())
        edge[s].add(t)
        edge[t].add(s)
        cnt[s] += 1
        cnt[t] += 1

    c4 = 0
    for i in range(1, n + 1):
        if cnt[i] == 4:
            c4 += 1

    if c4 != n:
        print(-1)
    else:
        for v2 in edge[1]:
            for v3 in edge[1]:
                if v2 in edge[v3]:
                    mark = [True] * (n + 1)
                    mark[1] = False
                    mark[v2] = False
                    res = [1, v2]
                    i = v3
                    try:
                        while True:
                            res.append(i)
                            mark[i] = False
                            if len(res) == n:
                                print(' '.join([str(x) for x in res]))
                                return
                            for e in edge[i]:
                                if e != i and mark[e] and res[-2] in edge[e]:
                                    i = e
                                    break
                            if not mark[i]:
                                raise StopIteration
                    except StopIteration:
                        pass

        print(-1)


def __starting_point():
    main()
__starting_point()