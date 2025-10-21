T = int(input())

for t in range(T):
  n = int(input())
  s = 1
  nxt = 2
  x = [1]
  while n > s:
    diff = n-s
    if diff <= nxt:
      x.append(diff)
      break
    x.append(nxt)
    s += nxt
    nxt *= 2
  x.sort()
  ans = ''
  for i in range(len(x)-1):
    v = x[i+1]-x[i]
    ans += str(v)+' '
  print(len(x)-1)
  print(ans[:-1])