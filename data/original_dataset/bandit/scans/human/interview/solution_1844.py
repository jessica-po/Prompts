from sys import *

maxn = 3 * 10 ** 5 + 5

fre = [0 for i in range(maxn)]
isprime = [1 for i in range(maxn)]
prime = []
divi = [0 for i in range(maxn)]
fact = [1] * 10

def nCr(n, r):
	if n < r:
		return 0
	if n == r:
		return 1
	pro = 1
	for i in range(r):
		pro *= (n - i)
	pro //= fact[r]
	return pro

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
for i in arr:
	if i is 1:
		print(1)
		return
	fre[i] += 1

divi[1] = n
for i in range(2, maxn):
	if isprime[i] is 1:
		prime.append(i)
	for j in range(1, maxn):
		if i * j >= maxn:
			break
		isprime[i * j] = 0
		divi[i] += fre[i * j]

for i in range(1, 10):
	fact[i] = fact[i - 1] * i

mobius = [0 for i in range(maxn)]

for i in range(1, maxn):
	mobius[i] = 1
for p in prime:
	if p * p >= maxn:
		break
	x = p * p
	for j in range(x, maxn, x):
		mobius[j] = 0
for p in prime:
	for j in range(p, maxn, p):
		mobius[j] *= -1 
		
for r in range(2, 10):
	coprime = 0
	for d in range(1, maxn):
		ncr = nCr(divi[d], r)
		coprime += mobius[d] * ncr
	if coprime > 0:
		print(r)
		return
print(-1)