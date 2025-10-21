a = list(input())
b = int(input())
a.sort()
a = a[::-1]
prefix = ""
while(len(a) > 0):
	for i in range(len(a)):
		num = prefix + a[i] + "".join(sorted(a[:i] + a[i + 1:]))
		if (int(num) <= b):
			prefix += a[i]
			a = a[:i] + a[i+1:]
			break
print(prefix)