n = int(input())
s = list(input())
m = n//2

if n%2 != 0:
  ans = "No"
else:
  for i in range(m):
    if s[i] != s[m+i]:
      ans = "No"
      break
    ans = "Yes"

print(ans)