n, m = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a = [-1] * 100001
for i in range(n):
	if a[f[i]] != -1:
		a[f[i]] = -2
	else:
		a[f[i]] = i
for i in b:
	if a[i] == -1:
		print('Impossible')
		return
for i in b:
	if a[i] == -2:
		print('Ambiguity')
		return
print('Possible')
for i in b:
	print(a[i] + 1, end=' ')