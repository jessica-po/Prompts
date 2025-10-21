#!/usr/local/bin/python3.3 -tt

import sys

def __starting_point():
    def _(f):
        for l in f:
            for i in l.split():
                yield int(i)

    g = _(sys.stdin)

    v = next(g)

    ar = []
    for i in range(9):
        ar.append((next(g), i + 1))

    dominant = min(ar, key=lambda t: (t[0], -t[1]))
    
    digits = v // dominant[0]

    v -= dominant[0] * digits

    ar = [(a - dominant[0], n) for a, n in ar if a > dominant[0] and n > dominant[1]]
    
    ar.sort(key=lambda x: (-x[1], x[0]))

    print(ar, file=sys.stderr)
    
    s = ''

    for a, n in ar:
        if a <= v:
            q = v // a
            v -= q * a
            s += str(n) * q

    s = '%s%s' % (s, str(dominant[1]) * (digits - len(s)))
    
    if s:
        print(s)
    else:
        print(-1)

__starting_point()