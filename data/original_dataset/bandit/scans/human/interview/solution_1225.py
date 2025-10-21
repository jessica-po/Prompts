h = int(input())
ans = 0
n = 0
while h != 0:
  ans += 2**n
  n += 1
  h = h//2
print(ans)