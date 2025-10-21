n = int(input())

a, b = [1], [0]

for i in range(n):
	new_b = a[:]
	a1 = a[:]
	a2 = a[:]
	a1.append(0)
	a2.append(0)
	for i in range(-1, -len(b) - 1, -1):
		a1[i] += b[i]
	for i in range(-1, -len(b) - 1, -1):
		a2[i] -= b[i]
	if max([abs(kek) for kek in a1]) < 2:
		a = a1
	elif max([abs(kek) for kek in a2]) < 2:
		a = a2
	else:
		print("oops")
		return
	b = new_b
print(len(a) - 1)
print(*(a[::-1]))
print(len(b) - 1)
print(*(b[::-1]))