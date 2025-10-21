3

import array
import math
import os
import sys


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, M, G):
    if N == 2:
        return [0, 1]

    degv = [set() for _ in range(5)]
    for i in range(M):
        d = len(G[i])
        if d == 0 or d >= 5:
            return []
        degv[d].add(i)

    layer_vcount = 1 << (N - 1)
    vs = degv[1]
    levels = bytearray(M)
    ans = []
    for level in range(1, N):
        #dprint('level', level, [x for x in levels])
        #dprint('vs', vs)
        #dprint('layer_vcount', layer_vcount)

        if len(vs) not in (layer_vcount - 1, layer_vcount):
            return []
        if len(vs) == layer_vcount - 1:
            if ans:
                return []
            if level == 1:
                sp_deg_off = -1
            else:
                sp_deg_off = 1
        else:
            sp_deg_off = 0
        #dprint('sp_deg_off', sp_deg_off)

        ndeg = 3 if level < N - 1 else 2
        us = set()
        ss = set()

        for v in vs:
            #dprint('v', v)
            levels[v] = level
            p = None
            for u in G[v]:
                if levels[u] == 0:
                    if p is not None:
                        return []
                    p = u
                    break
            #dprint('  p', p)
            if p is None:
                return []
            deg = len(G[p])
            #dprint('  deg', deg)

            if deg == ndeg:
                us.add(p)
            elif deg == ndeg + sp_deg_off:
                ss.add(p)
            elif sp_deg_off == 0 and deg == ndeg + 1:
                ss.add(p)
            else:
                return []

        #dprint('us', us)
        #dprint('ss', ss)

        if sp_deg_off != 0:
            if len(ss) != 1:
                return []
            (sp,) = list(ss)
            ans = [sp]
            us.add(sp)

        if sp_deg_off == 0:
            if level == N - 2:
                if ss:
                    return []
                if not ans:
                    li = list(us)
                    li.sort()
                    return li
            if len(ss) > 1:
                return []

        vs = us
        layer_vcount >>= 1

    return ans


def main():
    N = int(inp())
    M = (1 << N) - 2
    G = [[] for _ in range(M)]
    for _ in range(M - 1):
        a, b = [int(e) - 1 for e in inp().split()]
        G[a].append(b)
        G[b].append(a)

    ans = solve(N, M, G)
    print(len(ans))
    if ans:
        print(*[v + 1 for v in ans])


def __starting_point():
    main()

__starting_point()