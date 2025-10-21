import copy
n = int(input())
a = []
for i in range(n):
  s = int(input())
  a.append(s)
b = copy.copy(a)
a.sort(reverse=True)
c = b.index(a[0])
for j in b:
  if j == b[c]:
    print(a[1])
  else:
    print(a[0])