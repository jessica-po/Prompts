import sys

#f = open('input', 'r')
f = sys.stdin
n,k = list(map(int, f.readline().split()))
a = list(map(int, f.readline().split()))
aset = set(a)
st = []
failed = False
ai = 0
app = []
for p in range(1, n+1):
  if p in aset:
    while ai < k and (len(st)==0 or st[-1]!=p):
      st.append(a[ai])
      ai += 1
    if len(st) == 0 or st[-1] != p:
      failed = True
      break
    st.pop(-1)
    a += app[::-1]
    app = []
  else:
    if ai != k:
      st += a[ai:k]
      ai = k
    app.append(p)

if failed:
  print(-1)
else:
  print(' '.join(map(str, a + app[::-1])))