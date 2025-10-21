n = int(input())
p = list()
for i in range(n):
	p.append(set([int(x) for x in input().split()[1:]]))
for i in range(n):
	for j in range(n):
		if i != j:
			if p[i].issuperset(p[j]):
				print("NO")
				break
	else:
		print("YES")