n = int(input())
a = list(map(int, input().split()))
b = input()
r = 1000000000
l = -r
for i in range(4, n):
  if b[i - 1] != b[i]:
    if b[i] == '0':
      r = min(r, min(a[i - 4: i + 1]) - 1)
    else:
      l = max(l, max(a[i - 4: i + 1]) + 1)
print(l, r)