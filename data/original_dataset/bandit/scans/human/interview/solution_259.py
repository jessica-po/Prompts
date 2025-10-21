# AC
import sys


class Main:
    def __init__(self):
        self.buff = None
        self.index = 0

    def __next__(self):
        if self.buff is None or self.index == len(self.buff):
            self.buff = sys.stdin.readline().split()
            self.index = 0
        val = self.buff[self.index]
        self.index += 1
        return val

    def next_int(self):
        return int(next(self))

    def cal(self, s):
        if len(s) == 1:
            return s[0]
        if s[0] == 0:
            return self.cal(s[1:])
        v = 1
        for c in s:
            v *= c
        return v

    def solve(self):
        n = self.next_int()
        t = self.next_int()
        ii = 0
        tt = 10000000
        for i in range(0, n):
            fr = self.next_int()
            d = self.next_int()
            if fr < t:
                fr += (t - fr + d - 1) // d * d
            if fr < tt:
                tt = fr
                ii = i
        print(ii + 1)


def __starting_point():
    Main().solve()

__starting_point()