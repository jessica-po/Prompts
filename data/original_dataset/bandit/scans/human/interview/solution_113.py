def main():
	n, k = map(int, input().split())
	num_2 = 0
	num_5 = 0
	x = n
	while (x % 2 == 0):
		num_2 += 1
		x //= 2
		
	while (x % 5 == 0):
		num_5 += 1
		x //= 5
	num_2 = k - min(num_2, k)
	num_5 = k - min(num_5, k)
	print(n * 5 ** num_5 * 2 ** num_2)


main()