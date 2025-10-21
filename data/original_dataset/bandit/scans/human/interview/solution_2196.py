input()
a = list(map(int, input().split()))
b = []
i = j = 0
while i < len(a):
  while j < len(a) and a[j] == a[i]:
    j += 1
  if (j - i) % 2 == 1:
    b += [a[i]]
  i = j - (j - i) // 2
  for k in range(i, j):
    a[k] += 1
print(b[-1] - len(b) + 1)