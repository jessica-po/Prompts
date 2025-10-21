n = int(input())
a = list(map(int, input().split()))

ans = 0
t = 400
while t < 3201:
  for i in a:
    if i >= t-400 and i < t:
      ans += 1
      break
  t += 400

s = 0
for i in a:
  if i >= 3200: s += 1

if ans == 0: print(1, s)
else: print(ans, ans+s)