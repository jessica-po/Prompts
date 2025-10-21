k,a0,b0 = map(int,input().split())
a0,b0 = a0-1,b0-1

A = tuple(tuple(map(lambda c: int(c)-1,input().split())) for _ in range(3))
B = tuple(tuple(map(lambda c: int(c)-1,input().split())) for _ in range(3))

# A chose i and B chose j implies ? will choose ?[i][j]

score = lambda a,b: (int((a-b)%3==1),int((b-a)%3==1))

S = set()

cur = (a0,b0)

while cur not in S:
  S.add(cur)
  a,b = cur
  cur = (A[a][b],B[a][b])

pre = (0,0)
p = (a0,b0)
while k > 0 and p != cur:
  pre = tuple(c+d for c,d in zip(pre,score(*p)))
  a,b = p
  p = (A[a][b],B[a][b])
  k -= 1

if k == 0:
  print(*pre)
  return

# cycle length
L = 1
cnt = score(*cur)
a,b = cur
p = (A[a][b],B[a][b])

while p != cur:
  cnt = tuple(c+d for c,d in zip(cnt,score(*p)))
  L += 1
  a,b = p
  p = (A[a][b],B[a][b])

n = k//L
k -= (k//L)*L
cnt = (cnt[0]*n,cnt[1]*n)

suf = (0,0)
p = cur
while k > 0:
  suf = tuple(c+d for c,d in zip(suf,score(*p)))
  a,b = p
  p = (A[a][b],B[a][b])
  k -= 1

print(*(a+b+c for a,b,c in zip(pre,cnt,suf)))