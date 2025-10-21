# map(int, input())
t = int(input())
for i in range(t):
	s = sorted(input())
	if s[0] == s[-1]:
		print(-1)
		continue
	print(''.join(s))