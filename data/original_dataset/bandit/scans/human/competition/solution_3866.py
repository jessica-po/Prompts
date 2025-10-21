n = int(input())
if n % 2 == 0:
  print(-1)
else:
  print(*range(n))
  print(*range(n))
  print(*map(lambda x: x * 2 % n, range(n)))