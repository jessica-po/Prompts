d = [1, 1]
n = int(input())
while d[-1] < n:
	d.append(d[-1] + d[-2])
s = set(d)
res = ''
for i in range(1, n + 1):
	if i in s:
		res += 'O'
	else:
		res += 'o'
print(res)