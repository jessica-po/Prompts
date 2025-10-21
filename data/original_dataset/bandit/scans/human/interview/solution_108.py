s = list(input())
target = 'abcdefghijklmnopqrstuvwxyz'
ind_t = 0
ind_s = 0
while ind_s < len(s) and ind_t < 26:
  if ord(s[ind_s]) <= ord(target[ind_t]):
    s[ind_s] = target[ind_t]
    ind_t += 1
    ind_s += 1
  else:
    ind_s += 1
if ind_t == 26:
  print(''.join(s))
else:
  print(-1)