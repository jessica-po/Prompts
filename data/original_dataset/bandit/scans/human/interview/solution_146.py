n, k = list(map(int, input().split()))

t = list(map(int, input().split()))

d = [0 for _ in range(n)]

for _ in range(n):
  for i in range(n):
    if i % k != _ % k:
      d[_] += t[i]

print(max(abs(d[_]) for _ in range(n)))