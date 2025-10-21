n = int(input())
a = list(map(int, input().split()))
s = set(a)
m = {i: 0 for i in s}
for i in a:
	m[i] += 1
win = ''
for i in sorted(m)[::-1]:
	if m[i] % 2:
		win = 'Conan'
		break
if win:
	print(win)
else:
	print('Agasa')