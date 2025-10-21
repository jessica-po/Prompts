rd  = lambda: list(map(int, input().split()))

n, = rd()
a = [0] + rd() + [0]
for i in range(rd()[0]):
  x, y = rd()
  a[x-1] += y-1
  a[x+1] += a[x]-y
  a[x  ] = 0
print('\n'.join(map(str, a[1:1+n])))