#
# abc096 b
#
import sys
from io import StringIO
import unittest
from collections import Counter


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """6
aabbca"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
aaaaaaaaaa"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """45
tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir"""
        output = """9"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = input()

    ans = 0
    for i in range(1, N-1):
        x = Counter(S[0:i])
        y = S[i:]
        tmp = 0
        for j in list(x.keys()):
            if j in y:
                tmp += 1
        ans = max(ans, tmp)

    print(ans)


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()