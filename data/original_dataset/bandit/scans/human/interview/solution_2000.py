n = int(input())
a = [int(i) for i in input().split()]

def isp2(x):
	return (x >= 1) and ((x & (x - 1)) == 0)

p2 = [2 ** i for i in range(33)]

d = {}
for i in a:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1

k = 0
for i in d:
	for p in p2:
		j = p - i
		if j > i:
			break;
		if j in d:
			if i == j:
				k += d[i] * (d[i] - 1) // 2
			else:
				k += d[i] * d[j]

print(k)