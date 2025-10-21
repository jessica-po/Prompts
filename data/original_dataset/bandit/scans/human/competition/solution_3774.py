n, m = list(map(int, input().split()))
if n > m:
  n, m = m, n
if n == 1:
  print(([0, 0, 0, 0, 1, 2][m % 6] + m // 6 * 3) * 2)
  return
if n == 2:
  if m == 2:
    print(0)
  elif m == 3:
    print(4)
  elif m == 7:
    print(12)
  else:
    print(n * m)
  return
print((n * m) // 2 * 2)