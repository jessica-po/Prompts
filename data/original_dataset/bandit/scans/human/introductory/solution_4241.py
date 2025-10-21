s = input()
t = input()
m = 1000
for i in range(len(s) - len(t) + 1):
  c = 0
  for j in range(len(t)):
    if s[i + j] != t[j]:
      c += 1
  m = min(m, c)
print(m)