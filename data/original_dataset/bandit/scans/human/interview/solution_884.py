m = 998244353
n = 5050
mi = [1] * n
for i in range(2, n):
	mi[i] = (-(m//i) * mi[m%i]) % m;
f = [1] * n
g = [1] * n
for i in range(2, n):
	f[i] = (f[i-1] * i) % m
	g[i] = (g[i-1] * mi[i]) % m
	
def calc(x, y):
	s = 1
	p = f[x] * f[y]
	for i in range(1, min(x, y)+1):
		den = g[i] * g[x-i] * g[y-i]
		s += p * den % m
	return s

a, b, c = map(int, input().split())
ans = calc(a, b) * calc(b, c) * calc(c, a) % m
print(ans)