n = int(input())
x = input()
d = [0] * n
cd = 0
xp = []
for i in range(n):
	if x[i] == '[':
		d[i] = cd
		cd = cd + 1
	else:
		cd = cd - 1
		d[i] = cd
for i in range(n-1):
	xp.append((x[i], d[i]))
	if x[i] == '[' and x[i+1] == ']':
		xp.extend([(' ', d[i]), (' ', d[i]), (' ', d[i])])
xp.append((x[n-1], d[n-1]))
md = max(d)
h = md * 2 + 3
res = []
for i in range(h):
	l = [' ' for j in xp]
	res.append(l)
for i in range(len(xp)):
	for j in range(h):
		if xp[i][0] == '[' and j > xp[i][1] and j < h - xp[i][1] - 1:
			res[j][i] = '|'
		elif xp[i][0] == ']' and j > xp[i][1] and j < h - xp[i][1] - 1:
			res[j][i] = '|'
		elif xp[i][0] == '[' and (j == xp[i][1] or j == h - xp[i][1] - 1):
			res[j][i] = '+'
			res[j][i+1] = '-'
		elif xp[i][0] == ']' and (j == xp[i][1] or j == h - xp[i][1] - 1):
			res[j][i] = '+'
			res[j][i-1] = '-'

for i in range(h):
	print(''.join(res[i]))