# AC
import sys
sys.setrecursionlimit(1000000)


class Main:
    def __init__(self):
        self.buff = None
        self.index = 0

    def __next__(self):
        if self.buff is None or self.index == len(self.buff):
            self.buff = self.next_line()
            self.index = 0
        val = self.buff[self.index]
        self.index += 1
        return val

    def next_line(self):
        return sys.stdin.readline().split()

    def next_ints(self):
        return [int(x) for x in sys.stdin.readline().split()]

    def next_int(self):
        return int(next(self))

    def solve(self):
        a = next(self)
        b = next(self)
        d = 0
        g = 0
        for i in range(len(b)):
            if a[i] != b[i]:
                d += 1
            if i > 0 and b[i] != b[i - 1]:
                g += 1
        ans = 1 if d % 2 == 0 else 0
        for i in range(len(b), len(a)):
            if a[i] != b[-1]:
                d += 1
            if a[i - len(b)] != b[0]:
                d += 1
            d += g
            if d % 2 == 0:
                ans += 1
        print(ans)


def __starting_point():
    Main().solve()

__starting_point()