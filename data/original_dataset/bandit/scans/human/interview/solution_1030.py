n, p, k = map(int, input().split())

if (p - k) > 1:
	print('<<', end = ' ')

for i in range(p - k, p):
	if (i > 0):
		print(i, end = ' ')

print('(' + str(p) + ')', end = ' ')

for i in range(p + 1, p + k + 1):
	if (i < (n + 1)):
		print(i, end = ' ')

if (p + k) < n:
	print('>>', end = ' ')