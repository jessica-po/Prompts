def main():
	N, D = [int(n) for n in input().split(" ")]
	cnt = 0
	for i in range(N):
		X, Y = [int(x) for x in input().split(" ")]
		if X ** 2 + Y ** 2 <= D ** 2:
			cnt += 1
	print(cnt)

main()