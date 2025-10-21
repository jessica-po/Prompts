n, x = list(map(int, input().split()))
a = []
lst = 0
for i in range(1, 1 << n):
  if i ^ x > i:
    a.append(i ^ lst)
    lst = i
print(len(a))
print(' '.join(str(i) for i in a))