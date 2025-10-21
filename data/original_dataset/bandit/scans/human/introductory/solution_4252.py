n = int(input())
s = input()

res = 0
x_count = 0

for c in s:
	if c == 'x':
		x_count += 1
	else:
		x_count = 0

	if x_count > 2:
		res += 1


print(res)