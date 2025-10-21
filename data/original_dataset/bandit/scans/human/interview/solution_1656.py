s = input()
n = len(s)
p = [0] * (n+1)
for x in range(1, n):
	y = 0
	if s[x] == 'v' and s[x-1] == 'v':
		y = 1
	p[x+1] = p[x] + y
q = 0
sol = 0
for x in range(n-3, -1, -1):
	if s[x+1] == 'v' and s[x+2] == 'v':
		q += 1
	if s[x] == 'o':
		sol += q*p[x]
print(sol)