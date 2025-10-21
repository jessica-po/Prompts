match = 0
nonmatch = 0
count = 0

def calc_match(s, t, p):
  nonlocal match
  nonlocal nonmatch
  nonlocal count
  if p == len(s)-len(t):
    return
  if p+len(t) < len(s):
    if s[p+len(t)] == '?':
      count -= 1
    elif s[p+len(t)] == t[-1]:
      match -= 1
    else:
      nonmatch -= 1
  match, nonmatch = nonmatch, match
  if p+len(t) < len(s):
    if s[p] == '?':
      count += 1
    elif s[p] == 'a':
      match += 1
    else:
      nonmatch += 1

def init_match(s, t):
  nonlocal match
  nonlocal nonmatch
  nonlocal count
  p = len(s)-len(t)
  for i in range(len(t)):
    if s[p+i] == '?':
      count += 1
    elif s[p+i] == t[i]:
      match += 1
    else:
      nonmatch += 1



n = int(input())
s = input()
m = int(input())
t = ""
for i in range(m):
  if i%2==0:
    t = t + 'a'
  else:
    t = t + 'b'

init_match(s,t)

dp = []
for i in range(n+3):
  dp.append((0, 0))

p = n-m
while p >= 0:
  calc_match(s, t, p)
  if nonmatch == 0:
    if dp[p+1][0] == dp[p+m][0]+1:
      dp[p] = (dp[p+1][0], min(dp[p+1][1], dp[p+m][1]+count))
    elif dp[p+1][0] > dp[p+m][0]+1:
      dp[p] = dp[p+1]
    else:
      dp[p] = (dp[p+m][0]+1, dp[p+m][1]+count)
  else:
    dp[p] = dp[p+1]
  p -= 1

print(dp[0][1])