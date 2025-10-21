n = int(input())
s = sum(list(map(int, input().split())))
m = int(input())
for i in range(m):
	l, r = list(map(int, input().split()))
	s = max(s, l)
	if l <= s <= r:
		print(s)
		return
print(-1)