n, m, s, d = list(map(int, input().split()))

beg = [float('-inf')]
end = [float('-inf')]

a = [int(i) for i in input().split()]

for x in sorted(a):
	if (x - end[-1] > s + 1):
		beg.append(x)
		end.append(x)
	else:
		end[-1] = x

last = 0
R = []
J = []

for i in range(1, len(beg)):
	R.append(beg[i] - 1 - last)
	last = (beg[i] - 1)
	
	J.append(end[i] + 1 - last)
	last = (end[i] + 1)

ok = True
for x in J:
	if (x > d):
		ok = False
for x in R:
	if (x < s):
		ok = False


if ok:
	for i in range(len(R)):
		print('RUN', R[i])
		print('JUMP', J[i])
	if (last < m):
		print('RUN', m - last)
else:
	print('IMPOSSIBLE')