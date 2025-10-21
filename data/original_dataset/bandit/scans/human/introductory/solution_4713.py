N = int(input())
S = input()
res = 0
tmp = 0
for s in S:
  if s == 'I':
    tmp += 1
  elif s == 'D':
    tmp -= 1
  
  res = max(res, tmp)

print(res)