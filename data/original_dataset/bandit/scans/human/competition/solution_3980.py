n = int(input())
p = [i for i in range(n + 1)]

k = 1
while(2 * k <= n):
  k *= 2
m = n + 1
while m > 0:
  while k >= m:
    k //= 2
  for i in range(m - k):
    if k - i - 1 >= 0:
      p[k + i], p[k - i - 1] = p[k - i - 1], p[k + i]
  m = k - i - 1

print(n * (n + 1))
print(' '.join(map(str, p)))