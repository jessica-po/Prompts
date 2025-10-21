import sys

#f = open('input', 'r')
f = sys.stdin
n = int(f.readline())
a = list(map(int, f.readline().split()))

cnt = 0
for i in range(n):
  cnt += sum([1 for x in a[i+1:] if x < a[i]])

m = int(f.readline())
for _ in range(m):
  l, r = list(map(int, f.readline().split()))
  c = r-l
  cnt += (c*(c+1)//2)%2
  if cnt%2 == 0:
    print('even')
  else:
    print('odd')