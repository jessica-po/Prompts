n, m = map(int, input().split())
mi = 100000000000000
ts = ""
def num_d(a, b):
  t = 0
  for x in range(len(a)):
    if a[x] != b[x]:
      t += 1
  return t
s, t = input(), input()
for x in range(m-n+1):
  d = num_d(s, t[x:x+n])
  if d < mi:
    mi = d
    ts = t[x:x+n]
print(mi)
for x in range(n):
  if s[x] != ts[x]:
    print(x+1, end=" ")