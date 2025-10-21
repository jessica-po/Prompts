n = int(input())
lst = [int(x) for x in input().split()]
tmp = [False] * 100007
tmp2 = [False] * 100007

for x in lst:
	tmp[x] = True



answer, index = [], 1
for x in lst:
	if not tmp2[x] and x <= len(lst):
		answer.append(x)
		tmp2[x] = True
	else:
		while tmp[index]:
			index += 1
		tmp[index] = True
		answer.append(index)


print(' '.join(map(str, answer)))