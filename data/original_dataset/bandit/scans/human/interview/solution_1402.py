n, s = int(input()), 0
s1, s2 = str(input()), str(input())
b1, b2 = False, False
for i in range(n):
  if s1[i] != '?' and s2[i] != '?':
    if ord(s1[i]) < ord(s2[i]):
      b1 = True
    if ord(s1[i]) > ord(s2[i]):
      b2 = True
  s += (s1[i] == '?') + (s2[i] == '?')
ans1, ans2, ans3 = 1, 1, 1
for i in range(n):
  if s1[i] == '?' and s2[i] == '?':
    ans1 = (ans1 * 55) % 1000000007
    ans2 = (ans2 * 55) % 1000000007
    ans3 = (ans3 * 10) % 1000000007
  elif s1[i] == '?':
    ans1 = (ans1 * (ord(s2[i]) - ord('0') + 1)) % 1000000007
    ans2 = (ans2 * (10 - ord(s2[i]) + ord('0'))) % 1000000007
  elif s2[i] == '?':
    ans1 = (ans1 * (10 - ord(s1[i]) + ord('0'))) % 1000000007
    ans2 = (ans2 * (ord(s1[i]) - ord('0') + 1)) % 1000000007
print((10 ** s - (not b2) * ans1 - (not b1) * ans2 + (not b1 and not b2) * ans3) % 1000000007)