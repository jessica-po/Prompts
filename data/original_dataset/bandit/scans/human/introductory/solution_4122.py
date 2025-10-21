H, n = list(map(int, input().split()))
d = list(map(int, input().split()))

t = 0
miPt = H
for a in d:
  t += 1
  H += a
  miPt = min(miPt, H)
  if H <= 0:
    print(t)
    return

if sum(d) >= 0:
  print(-1)
  return

jump = max(0, miPt // -sum(d) - 2)
H -= jump * -sum(d)
t += n * jump
for i in range(100000000000000000):
  t += 1
  H += d[i % n]
  if H <= 0:
    print(t)
    return