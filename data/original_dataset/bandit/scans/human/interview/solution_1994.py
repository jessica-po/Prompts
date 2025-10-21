s = input()
n = len(s)
p = [0] * n
k = 0
for i in range(1, n):
  while k != 0 and s[k] != s[i]:
    k = p[k - 1]
  if s[k] == s[i]:
    k += 1
  p[i] = k
a = []
k = n
while k != 0:
  a += [k]
  k = p[k - 1]
c = [0] * (n + 1)
for i in range(n):
  c[p[i]] += 1
for i in range(n - 1, 1, -1):
  c[p[i - 1]] += c[i]
print(len(a))
for t in reversed(a):
  print(t, c[t] + 1)