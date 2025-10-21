def mask(n):
  if not n: return 0;
  m = 1
  while not (m & n):
    m *= 2
  return m
  
n, T = list(map(int, input().split()))
for t in range(T):
  cur = int(input())
  for ch in input():
    m = mask(cur)
    #print(ch, ":", m, cur, "->", end = " ")
    if ch == "U":
      next = (cur - m) | (m * 2)
      if next < n: cur = next
    elif ch == "L" and m > 1:
      cur -= m//2
    elif ch == "R" and m > 1:
      cur += m//2
    #print(cur)
  print(cur)