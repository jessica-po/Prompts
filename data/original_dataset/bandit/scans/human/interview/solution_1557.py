h1, a1, c1 = list(map(int, input().split()))
h2, a2 = list(map(int, input().split()))
d = []
while h2 > 0:
	if h2 <= a1:
		h2 -= a1
		d.append('STRIKE')
	else:
		if h1 <= a2:
			d.append('HEAL')
			h1 += c1
		else:
			d.append('STRIKE')
			h2 -= a1
	h1 -= a2
print(len(d))
for i in d:
	print(i)