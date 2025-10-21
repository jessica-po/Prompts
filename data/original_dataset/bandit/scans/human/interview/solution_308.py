x, y, n, c = 0, 0, 0, 0
def suma_impares(m):
	return m * m
def suma_n(m):
	return m * (m - 1) // 2
def cnt(t):
	u, d, l, r = x + t, x - t, y - t, y + t
	suma = t ** 2 + (t + 1) ** 2
	if u > n: suma -= suma_impares(u - n)
	if d < 1: suma -= suma_impares(1 - d)
	if l < 1: suma -= suma_impares(1 - l)
	if r > n: suma -= suma_impares(r - n)
	if 1 - l > x - 1 and 1 - d > y - 1:
		suma += suma_n(2 - l - x)
	if r - n > x - 1 and 1 - d > n - y:
		suma += suma_n(r - n - x + 1)
	if 1 - l > n - x and u - n > y - 1:
		suma += suma_n(1 - l - n + x)
	if u - n > n - y and r - n > n - x:
		suma += suma_n(u - n - n + y)
	return suma
	
n, x, y, c = input().split()
n, x, y, c = int(n), int(x), int(y), int(c)
#for i in range(10):
#	print(i, cnt(i))
ini, fin = 0, int(1e9)
cont = int(1e9)
while cont > 0:
	m = ini
	paso = cont // 2
	m += paso
	if cnt(m) < c:
		ini = m + 1
		cont -= paso + 1
	else:
		cont = paso
print(ini)