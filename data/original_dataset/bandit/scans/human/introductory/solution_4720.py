N = int(input())
ans = 0
for _ in range(N):
  a, b = map(int, input().split())
  ans += b - a + 1
print(ans)