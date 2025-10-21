num = input()

cnt = 0
for _ in range(int(num)):
  a = input()
  b = list(a)
  if b[0] == b[2]:
    cnt += 1
    if cnt >= 3:
      print('Yes')
      break
  else:
    cnt = 0

if cnt <= 2:
  print('No')