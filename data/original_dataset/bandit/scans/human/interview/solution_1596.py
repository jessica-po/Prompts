from itertools import groupby

s = input()
n = len(s)

if "w" in s or "m" in s:
	print("0")
	return

mod = 10**9+7
fib = [1, 1]
for i in range(2, n+1):
	fib.append((fib[-1]+fib[-2])%mod)

res = 1

for k, g in groupby(s):
	if k=="u" or k=="n":
		l = len(list(g))
		res *= fib[l]
		res %= mod

print(res)