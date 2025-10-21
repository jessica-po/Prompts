n, k = map(int, input().split())
j = 0
for i in input():
  if i == '.':
    j = 0
  else:
    j += 1
    if j >= k:
      print("NO")
      break
else:
  print("YES")