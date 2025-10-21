#!/usr/bin/env python3
# 600D_circles.py - Codeforces.com/problemset/problem/600/D by Sergey 2015

import unittest
import sys
import math
import decimal

###############################################################################
# Circles Class (Main Program)
###############################################################################


def sin(x):
    decimal.getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    return +s


def cos(x):
    decimal.getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    return +s


def pi():
    decimal.getcontext().prec += 2
    three = decimal.Decimal(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s


def asin(x):
    decimal.getcontext().prec += 2
    b, e = -pi()/2, pi()/2
    while True:
        mid = (b + e) / 2
        if e == mid or b == mid:
            break
        if sin(mid) <= x:
            b = mid
        else:
            e = mid
    decimal.getcontext().prec -= 2
    return +b


def acos(x):
    return pi() / 2 - asin(x)


class Circles:
    """ Circles representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.xa, self.ya, self.ra] = list(map(decimal.Decimal, uinput().split()))
        [self.xb, self.yb, self.rb] = list(map(decimal.Decimal, uinput().split()))

        decimal.getcontext().prec = 40

        self.l = ((self.xb - self.xa)**2 + (self.yb - self.ya)**2).sqrt()
        self.p = (self.ra + self.rb + self.l)/2

        if self.l >= self.p:
            self.sa = 0
            self.sb = 0
        elif self.ra >= self.p:
            self.sa = 0
            self.sb = self.rb**2 * decimal.Decimal.from_float(math.pi)
        elif self.rb >= self.p:
            self.sa = self.ra**2 * decimal.Decimal.from_float(math.pi)
            self.sb = 0
        else:
            self.aa = 2 * acos(
                (self.ra**2 - self.rb**2 + self.l**2) /
                (2 * self.ra * self.l))
            self.ab = 2 * acos(
                (self.rb**2 - self.ra**2 + self.l**2) /
                (2 * self.rb * self.l))
            self.sa = self.ra**2 * (self.aa - sin(self.aa)) / 2
            self.sb = self.rb**2 * (self.ab - sin(self.ab)) / 2

    def calculate(self):
        """ Main calcualtion function of the class """

        result = self.sa + self.sb

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Circles class testing """

        # Constructor test
        test = "0 0 4\n6 0 4"
        d = Circles(test)
        self.assertEqual(d.l, 6)

        # Sample test
        self.assertEqual(Circles(test).calculate()[:8], "7.252988")

        # Sample test
        test = "0 0 5\n11 0 5"
        self.assertEqual(Circles(test).calculate(), "0")

        # Sample test
        test = "44721 999999999 400000000\n0 0 600000000"
        self.assertEqual(Circles(test).calculate()[:9], "0.0018834")

        # My tests
        test = ""
        # self.assertEqual(Circles(test).calculate(), "0")

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
        d = Circles(test)
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
    sys.stdout.write(Circles().calculate())

__starting_point()