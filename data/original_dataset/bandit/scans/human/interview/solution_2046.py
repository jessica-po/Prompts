n = int(input())
a = list(map(int, input().split()))
s = set()
j = 0
i = n
while i != 0:
	if a[j] == i:
		print(i)
		j += 1
		i -= 1
	else:
		while j < n and a[j] != i:
			s.add(a[j])
			j += 1
			print()
		s.add(i)
		while i > 0 and i in s:
			print(i, end = ' ')
			i -= 1