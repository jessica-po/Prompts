"""This code was written by
Russell Emerine - linguist,
mathematician, coder,
musician, and metalhead."""

n = int(input())
for _ in range(n):
  c, s = list(map(int, input().split()))
  a = s // c
  r = s % c
  print((c - r) * a ** 2 + r * (a + 1) ** 2)