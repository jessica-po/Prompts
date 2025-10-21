n = int(input())

def pr(x):
	for i in range(2, x):
		if x % i == 0:
			return False
	return True

e = []
for i in range(n):
	e += [[i, (i+1) % n]]
x = n
u = 0
v = n // 2
while not pr(x):
	e += [[u, v]]
	x += 1
	u += 1
	v += 1

print(x)
for g in e:
	print(g[0]+1, g[1]+1)