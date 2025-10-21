n = int(input())
a = list(map(int, input().split()))
a = [0] + a
for i in range(1, n):
  a[i] += a[i - 1]
mi = min(a)
a = list([x - mi + 1 for x in a])
print(-1 if set(a) != set(range(1, n + 1)) else ' '.join(map(str, a)))