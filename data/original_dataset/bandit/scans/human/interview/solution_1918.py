n = input()
s = [int(x) for x in input().split(' ')]
g = input()
A = 0
B = 0
for i in range(len(g)):
	if g[i] == 'A':
		A += s[i]
	else:
		B += s[i]

startA, startB = A, B
maximum = B

for i in range(len(g)):
	if g[i] == 'A':
		A -= s[i]
		B += s[i]
	else:
		A += s[i]
		B -= s[i]
	if B > maximum:
		maximum = B

A, B = startA, startB

for i in reversed(range(len(g))):
	if g[i] == 'A':
		A -= s[i]
		B += s[i]
	else:
		A += s[i]
		B -= s[i]
	if B > maximum:
		maximum = B

print(maximum)