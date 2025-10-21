n = int(input())

d = {}

for i in range(n):
	s = input()
	if s in d:
		d[s] += 1
	else:
		d[s] = 1

print(d[max(d,key=d.get)])