n = int(input())
a = list(map(int, input().split()))
b = [0]
for i in range(1, n):
	if a[i]*2 <= a[0]:
		b += [i]
u=0
v=0
for i in range(n):
	if i in b:
		u += a[i]
	else:
		v += a[i]
if u > v:
	print(len(b))
	for x in b:
		print(x+1, end=' ')
else:
	print('0')