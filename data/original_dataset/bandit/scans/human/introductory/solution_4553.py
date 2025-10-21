a,b = list(map(int, input().split()))
s = input()
count = 0
ans = 'Yes'
for i in range(a+b+1):
  if i == a:
    if s[i] != '-':
      ans = 'No'
      break
  else:
    if s[i] == '-':
      ans = 'No'
      break
print(ans)