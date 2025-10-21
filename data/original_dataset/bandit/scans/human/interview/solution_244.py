def main():
	n = int(input())
	k = int(input())
	n %= 6
	a = [0, 1, 2]
	for i in range(1, n + 1):
		if (i % 2 == 1):
			a[0], a[1] = a[1], a[0]
		else:
			a[1], a[2] = a[2], a[1]
	print(a[k])


main()