n, m = list(map(int, input().split()))
s = list(input())
a = []
for _ in range(m):
	l, r, c1, c2 = input().split()
	l, r = int(l) - 1, int(r) - 1
	for i in range(l, r + 1):
		if s[i] == c1:
			s[i] = c2
print(''.join(s))