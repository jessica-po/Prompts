s = list(input())

ans = 0
for i in range(1, len(s)):
  if s[i] == s[i-1]:
    ans += 1
    if s[i] == '1':
      s[i] = '0'
    else:
      s[i] = '1'
    
print(ans)