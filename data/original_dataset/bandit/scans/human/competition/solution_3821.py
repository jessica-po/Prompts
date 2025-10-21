n = int(input())
a = list(map(float, input().split()))
a.sort()
s = a[-1]
p = 1 - a[-1]
for i in range(n - 2, -1, -1):
	if s < s * (1 - a[i]) + a[i] * p:
		s = s * (1 - a[i]) + a[i] * p
		p *= (1 - a[i])
print('%.9lf' % s)