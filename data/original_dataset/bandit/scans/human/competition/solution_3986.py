import string

rd = lambda: list(map(int, input().split()))

n, k = rd()
if k>26 or k>n or k==1 and n>1:
  print(-1)
elif k==1 and n==1:
  print('a')
else:
  print(('ab'*(n+1>>1))[:n-k+2]+string.ascii_lowercase[2:k])