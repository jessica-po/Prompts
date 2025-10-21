#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io

from collections import defaultdict
from itertools import combinations


def solve(n, m, pairs):
    # return: minimum possible sum of their recognitions
    assert 3 <= n <= 4000  # number of warioor
    assert 0 <= m <= 4000  # number of pairs of warriors knowing each other
    # for (a, b) in pairs:
    #     assert 1 <= a < b <= n 

    recognitions = defaultdict(set)

    for (a, b) in pairs:
       recognitions[a].add(b)
       recognitions[b].add(a)

    minr = float('inf')

    for candidate, recognition in [(c, rs) for c, rs in list(recognitions.items()) if len(rs) > 1]:
        for c2, c3 in [(a, b) for a, b in combinations(recognition, 2)
                                if a in recognitions[b]]:
            sum_r = sum([len(recognitions[x]) for x in [candidate, c2, c3]])
            minr = min([sum_r, minr])
    if minr == float('inf'):
        return -1
    else:
        return minr - 2 * 3



def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints(n):
        return [getint() for _ in range(n)]

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    n, m = getints_line()
    return [n, m, getints_lines(m)]


def iosolve():
    return str(solve(*getinput()))
    # return 'YES' if solve(*getinput()) else 'NO' # for boolean output
    # return '\n'.join(map(str, solve(*getinput()))) # for multiple line output


def main():
    if sys.stdin.isatty():
        test()
    stdin_lines = getstdin_lines()
    sys.stdin = io.StringIO('\n'.join(stdin_lines))
    if stdin_lines:
        print(iosolve())
    else:
        test()


def test():
    IO_TEST_CASES = [

        (
            # INPUT
            '''\
5 6
1 2
1 3
2 3
2 4
3 4
4 5
            ''',
            # EXPECT
            '''\
2
            '''
        ),

        (
            # INPUT
            '''\
7 4
2 1
3 6
5 1
1 7
            ''',
            # EXPECT
            '''\
-1
            '''
        ),


    ]

    # List[(List[arg for solve()], expect)]
    TEST_CASES = [
        # ([], None),
    ]

    # You do need to see below
    import unittest  # to save memory, import only if test required
    import sys
    import io

    class Assert(unittest.TestCase):
        def equal(self, a, b):
            self.assertEqual(a, b)

        def float_equal(self, actual, expect, tolerance):
            self.assertTrue(expect - tolerance < actual < expect + tolerance)

    art = Assert()

    for inputs, expect in TEST_CASES:
        art.equal(solve(*inputs), expect)

    for stdin, expect in IO_TEST_CASES:
        sys.stdin = io.StringIO(stdin.strip())
        art.equal(iosolve(), expect.strip())
        # art.float_equal(float(iosolve()), float(expect.strip()), 10 ** -6)


def getstdin_lines():
    stdin = []
    while 1:
        try:
            stdin.append(input())
        except EOFError:
            break
    return stdin

def __starting_point():
    main()

__starting_point()