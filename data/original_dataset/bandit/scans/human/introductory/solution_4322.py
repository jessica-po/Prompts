# AC
import sys


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

    def next_line(self, _map=str):
        return list(map(_map, sys.stdin.readline().split()))

    def next_int(self):
        return int(next(self))

    def solve(self):
        n = self.next_int()
        x = sorted([self.next_int() for _ in range(0, n)])
        ml = -1
        _i = 0
        _j = 0
        j = 0
        for i in range(0, n):
            j = max(j, i)
            while j + 1 < n and x[j + 1] == x[i]:
                j += 1
            while j + 2 < n and x[j + 2] == x[j] + 1:
                j += 2
                while j + 1 < n and x[j + 1] == x[j]:
                    j += 1
            jj = j
            if j + 1 < n and x[j + 1] == x[j] + 1:
                jj += 1
            if jj - i > ml:
                ml = jj - i
                _i = i
                _j = jj
        a = []
        b = []
        i = _i
        while i <= _j:
            a.append(x[i])
            i += 1
            while i <= _j and x[i] == a[-1]:
                b.append(x[i])
                i += 1
        print(ml + 1)
        print(' '.join([str(x) for x in (a + b[::-1])]))


def __starting_point():
    Main().solve()

__starting_point()