N = int(input())
s = []

for i in range(N):
  s.append(int(input()))
  
S = sum(s)

if S%10 != 0:
  print(S)
else:
  b = True
  for j in range(N):
    if  s[j]%10 == 0:
      continue
    else:
      b = False
  if b:
    print(0)
  else:
    s.sort()
    for k in range(N):
      if s[k]%10 != 0:
        print(S-s[k])
        break