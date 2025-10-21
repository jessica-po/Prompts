def main():
	n, l = map(int, input().split())

	x = list(map(int, input().split()))
	y = list(map(int, input().split()))

	x.append(x[0] + l)
	y.append(y[0] + l)

	a = [x[i + 1] - x[i] for i in range(n)]
	b = [y[i + 1] - y[i] for i in range(n)]

	for i in range(n):
		if (a == b[i:] + b[:i]):
			print("YES")
			return
	print("NO")


main()