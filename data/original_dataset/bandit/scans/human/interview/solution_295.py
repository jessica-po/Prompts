from math import sqrt

def phi(u):
	ans = u
	for i in range(2, int(sqrt(n)) + 1):
		if u % i == 0:
			while u % i == 0:
				u = u / i
			ans = ans - int(ans / i)
	if n > 1:
		ans = ans - int(ans / n)
	return ans

def binpow(u, a, mod):
	ans = 1
	if a == 0:
		return 1;
	while a > 0:
		if a % 2 == 0:
			u = (u ** 2) % mod
			a = int(a / 2)
		else :
			ans = (ans * u) % mod
			a = a - 1
	return int(ans)

n = int(input())

b1 = 1
b2 = 0
nn = n
for i in range(2, int(sqrt(n)) + 1):
	if n%i == 0 :
		while nn % i == 0:
			b1 = b1 * i
			nn = nn / i
		b2 = int(n / b1)
		break

if b2 < 2:
	print("NO")
	return
a1 = b1 - binpow(b2, phi(b1) - 1, b1)
a2 = b2 - int((a1*b2+1)/b1)
print("YES")
print(2)
print(a1, b1)
print(a2, b2)