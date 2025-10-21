n = int(input())
ans = 0
for i in range(n):
	s, d = list(map(int, input().split()))
	visit = s
	while visit <= ans:
		visit += d
	ans = visit
print(ans)