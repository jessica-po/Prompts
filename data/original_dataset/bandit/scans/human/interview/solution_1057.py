input()
s = input()
r1 = 1
f = s[0]
for c in s:
	if c != f:
		break
	r1 += 1
r2 = 1
p = s[-1]
for c in s[::-1]:
	if c != p:
		break
	r2 += 1
if f == p:
	print((r1 * r2) % 998244353)
else:
	print((r1 + r2 - 1) % 998244353)