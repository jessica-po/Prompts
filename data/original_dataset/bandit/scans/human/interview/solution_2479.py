import sys

def solve():
      input = sys.stdin.readline
      N, Q = map(int, input().split())
      total = (N - 2) ** 2
      rb = N
      db = N
      D = [N] * (N + 1)
      R = [N] * (N + 1)
      for _ in range(Q):
            a, b = map(int, input().split())
            if a == 1: #横向き
                  if b < db:
                        total -= (rb - 2)
                        for i in range(b, db): R[i] = rb
                        db = b
                  else:
                        total -= (R[b] - 2)
            else: #縦向き
                  if b < rb:
                        total -= (db - 2)
                        for i in range(b, rb): D[i] = db
                        rb = b
                  else:
                        total -= (D[b] - 2)

      print(total)

      return 0

def __starting_point():
      solve() 
__starting_point()