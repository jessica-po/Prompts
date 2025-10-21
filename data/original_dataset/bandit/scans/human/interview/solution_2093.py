import sys

class RangeBit:
    def __init__(self, n):
        sz = 1
        while n >= sz:
            sz *= 2
        self.size = sz
        self.dataAdd = [0 for _ in range(sz)]
        self.dataMul = [0 for _ in range(sz)]

    def sum(self, i):
        assert i > 0
        add, mul, start = 0, 0, i
        while i > 0:
            add += self.dataAdd[i]
            mul += self.dataMul[i]
            i -= i & -i
        return mul * start + add

    def add(self, left, right, by):
        assert 0 < left <= right
        self._add(left, by, -by * (left - 1))
        self._add(right, -by, by * right)

    def _add(self, i, mul, add):
        assert i > 0
        while i < self.size:
            self.dataAdd[i] += add
            self.dataMul[i] += mul
            i += i & -i

n = int(input())
l = list(map(int, sys.stdin.readline().split()))

queries = []
for i in range(n):
    if min(l[i], n) >= i+2:
        queries.append((i+2, min(l[i], n), i+1))

result = 0

a = sorted(list(zip(list(range(1, n+1)), l)) + queries, key=lambda x:(-x[-1], len(x)))
ft = RangeBit(n+1)

for el in a:
    #print(el)
    if len(el) == 2: #update
        ind, val = el
        ft.add(ind, ind, 1)
    else: #query
        fr, to, val = el
        # print(fr, to, val)
        # print(ft.sum(to) - (ft.sum(fr - 1) if fr > 1 else 0))
        result += ft.sum(to) - (ft.sum(fr - 1) if fr > 1 else 0)

print(result)