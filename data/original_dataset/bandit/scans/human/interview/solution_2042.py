#!/usr/bin/env python3
# 598D_Igor.py - Codeforces.com/problemset/problem/598/D by Sergey 2015

import unittest
import sys
from collections import deque

###############################################################################
# Igor Class (Main Program)
###############################################################################


def empty_around(i, rc, n, m, nw, mw):
    w = 32
    r = (i // m) // w
    c = (i % m) // w
    j = r * mw + c
    if j < len(rc):
        if rc[j] == 0:
            rc[j] = 1
            return True, r, c
    return False, 0, 0


def fill_around(a, r0, c0, to_visit, visited, n, m):
    w = 32
    for r in range(w):
        for c in range(w):
            i = (r0 * w + r) * m + (c0 * w + c)
            if (r == 0 or r == w - 1 or c == 0 or c == w - 1):
                if a[i] == 0:
                    to_visit.append(i)
                    a[i] = 1
            else:
                a[i] = 2
                visited.append(i)


class Igor:
    """ Igor representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        self.result = []
        w = 32
        n, m, k = [int(x) for x in uinput().split()]
        d0, d1, d2, d3 = -m, 2*m, -m-1, 2
        a = []
        rc = []
        rr = []
        mw = m // w
        nw = n // w
        for _ in range(n):
            row = [(0 if v == '.' else 3) for v in uinput()]
            a += row
            rc += [sum(row[i*w:i*w+w]) for i in range(mw)]
        for i in range(nw):
            j = i*mw*w
            rr += [sum([rc[j+u*mw+v] for u in range(w)]) for v in range(mw)]
        to_visit = deque()
        for _ in range(k):
            x0, y0 = [int(x)-1 for x in uinput().split()]
            i0 = x0*m+y0
            step = 0
            if a[i0] > 3:
                self.result.append(a[i0])
            else:
                ans = 0
                to_visit.append(i0)
                visited = deque()
                step += 1
                while to_visit:
                    i = to_visit.pop()
                    if a[i] == 2:
                        continue
                    visited.append(i)
                    if step % w == 1:
                        e, r0, c0 = empty_around(i, rr, n, m, nw, mw)
                    else:
                        e = False
                    a[i] = 2
                    if e:
                        fill_around(a, r0, c0, to_visit, visited, n, m)
                    for d in (d0, d1, d2, d3):
                        i += d
                        if a[i] == 0:
                            to_visit.append(i)
                            a[i] = 1
                        elif a[i] == 3:
                            ans += 1
                self.result.append(ans)
                for i in visited:
                    a[i] = ans

    def calculate(self):
        """ Main calcualtion function of the class """

        return str("\n".join(map(str, self.result)))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Igor class testing """

        # Constructor test
        test = "5 6 3\n******\n*..*.*\n******\n*....*\n******\n2 2\n2 5\n4 3"
        d = Igor(test)

        # Sample test
        self.assertEqual(Igor(test).calculate(), "6\n4\n10")

        # Sample test
        test = ""
        # self.assertEqual(Igor(test).calculate(), "0")

        # Sample test
        test = ""
        # self.assertEqual(Igor(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Igor(test).calculate(), "0")

        # Time limit test
        # self.time_limit_test(5000)

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit

        # Random inputs
        test = str(nmax) + " " + str(nmax) + "\n"
        numnums = [str(i) + " " + str(i+1) for i in range(nmax)]
        test += "\n".join(numnums) + "\n"
        nums = [random.randint(1, 10000) for i in range(nmax)]
        test += " ".join(map(str, nums)) + "\n"

        # Run the test
        start = timeit.default_timer()
        d = Igor(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print(("\nTimelimit Test: " +
              "{0:.3f}s (init {1:.3f}s calc {2:.3f}s)".
              format(stop-start, calc-start, stop-calc)))

def __starting_point():

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(Igor().calculate())

__starting_point()